// GitHub access, read-only, in the visitor's browser. No server, no cookies, no tracking.
// The token is typed by its owner, kept only in this tab's memory (gone on reload or close)
// and sent only to api.github.com. This page only reads: get() refuses any other method.
const API = 'https://api.github.com';
let token = '';

async function get(path) {
  const r = await fetch(API + path, {
    method: 'GET',
    credentials: 'omit',
    referrerPolicy: 'no-referrer',
    headers: { accept: 'application/vnd.github+json', 'x-github-api-version': '2022-11-28', authorization: 'Bearer ' + token },
  });
  const left = r.headers.get('x-ratelimit-remaining');
  if (left !== null) $('#rate').textContent = `GitHub API calls left this hour: ${left}`;
  if (!r.ok) return { error: r.status };
  return { data: await r.json(), link: r.headers.get('link') || '' };
}

async function all(path, max = 1000) {
  const out = [];
  let url = path + (path.includes('?') ? '&' : '?') + 'per_page=100';
  while (url && out.length < max) {
    const r = await get(url);
    if (r.error) return out.length ? out : r;
    out.push(...r.data);
    const next = /<https:\/\/api\.github\.com([^>]+)>;\s*rel="next"/.exec(r.link);
    url = next ? next[1] : '';
  }
  return out;
}

const $ = s => document.querySelector(s);
const el = (tag, text, cls) => { const e = document.createElement(tag); if (text != null) e.textContent = text; if (cls) e.className = cls; return e; };
const day = s => (s ? s.slice(0, 10) : '-');
const why = code => ({ 401: 'the token was refused', 403: 'the token may not read this', 404: 'not found, or the token may not see it' }[code] || `HTTP ${code}`);

function table(caption, head, rows) {
  const wrap = el('div', null, 'scroll');
  wrap.tabIndex = 0; wrap.setAttribute('role', 'region'); wrap.setAttribute('aria-label', caption);
  const t = el('table');
  t.append(el('caption', caption));
  const thead = el('thead'), tr = el('tr');
  head.forEach(h => { const th = el('th', h); th.scope = 'col'; tr.append(th); });
  thead.append(tr); t.append(thead);
  const tb = el('tbody');
  rows.forEach(cells => { const r = el('tr'); cells.forEach(c => r.append(c instanceof Node ? (c.tagName === 'TD' ? c : wrapTd(c)) : el('td', String(c)))); tb.append(r); });
  if (!rows.length) { const r = el('tr'), td = el('td', 'None'); td.colSpan = head.length; r.append(td); tb.append(r); }
  t.append(tb); wrap.append(t);
  return wrap;
}
function wrapTd(node) { const td = el('td'); td.append(node); return td; }
function link(href, text) { const a = el('a', text); a.href = href; a.rel = 'noopener noreferrer'; return a; }

async function overview() {
  const out = $('#out');
  out.textContent = '';
  $('#status').textContent = 'Reading your account...';
  const me = await get('/user');
  if (me.error) { $('#status').textContent = `Could not read your account: ${why(me.error)}.`; return; }
  const u = me.data;
  $('#status').textContent = `Signed in to the API as ${u.login}. Reading repositories...`;
  const repos = await all('/user/repos?sort=pushed&affiliation=owner,collaborator,organization_member');
  if (repos.error) { $('#status').textContent = `Could not list repositories: ${why(repos.error)}.`; return; }

  const pub = repos.filter(r => !r.private).length;
  const admin = repos.filter(r => r.permissions && r.permissions.admin).length;
  const owners = [...new Set(repos.map(r => r.owner.login))].sort();
  $('#status').textContent = `${u.login}: ${repos.length} repositories (${pub} public, ${repos.length - pub} private), across ${owners.length} owners; admin on ${admin}.`;

  const filter = el('p');
  const lab = el('label', 'Show owner '); lab.htmlFor = 'owner';
  const sel = el('select'); sel.id = 'owner';
  sel.append(new Option('All owners', ''));
  owners.forEach(o => sel.append(new Option(o, o)));
  filter.append(lab, sel);
  out.append(filter);

  const holder = el('div');
  out.append(holder);
  const draw = () => {
    const list = repos.filter(r => !sel.value || r.owner.login === sel.value);
    holder.textContent = '';
    holder.append(table('Repositories, most recently pushed first', ['Repository', 'Visibility', 'Your role', 'Default branch', 'Last push', 'Detail'],
      list.map(r => {
        const b = el('button', 'Access', 'small');
        b.type = 'button';
        b.setAttribute('aria-label', `Access for ${r.full_name}`);
        b.addEventListener('click', () => detail(r));
        const role = r.permissions ? (r.permissions.admin ? 'admin' : r.permissions.maintain ? 'maintain' : r.permissions.push ? 'write' : r.permissions.triage ? 'triage' : 'read') : '-';
        return [link(r.html_url, r.full_name), r.private ? 'private' : 'public', role, r.default_branch || '-', day(r.pushed_at), b];
      })));
  };
  sel.addEventListener('change', draw);
  draw();
}

async function detail(r) {
  const box = $('#detail');
  box.textContent = '';
  const h = el('h2', `Access: ${r.full_name}`);
  h.tabIndex = -1;
  box.append(h);
  h.focus();
  const p = `/repos/${r.full_name}`;
  const [collab, teams, keys, hooks, rules, pages] = await Promise.all([
    all(p + '/collaborators?affiliation=all'), all(p + '/teams'), all(p + '/keys'), all(p + '/hooks'), all(p + '/rulesets'), get(p + '/pages'),
  ]);
  const part = (title, res, head, map) => {
    if (res.error) { box.append(el('p', `${title}: ${why(res.error)}.`, 'note')); return; }
    box.append(table(title, head, res.map(map)));
  };
  part('People with access', collab, ['Login', 'Role'], c => [link(c.html_url, c.login), c.role_name || '-']);
  part('Teams', teams, ['Team', 'Permission'], t => [t.name, t.permission || '-']);
  part('Deploy keys', keys, ['Title', 'Read only', 'Added'], k => [k.title, k.read_only ? 'yes' : 'no, can push', day(k.created_at)]);
  part('Webhooks', hooks, ['Sends to', 'Active', 'Events'], w => [w.config && w.config.url ? new URL(w.config.url).host : '-', w.active ? 'yes' : 'no', (w.events || []).join(', ')]);
  part('Rulesets', rules, ['Name', 'Target', 'Enforcement'], s => [s.name, s.target || '-', s.enforcement || '-']);
  if (pages.error) box.append(el('p', pages.error === 404 ? 'Pages: not switched on.' : `Pages: ${why(pages.error)}.`, 'note'));
  else box.append(el('p', `Pages: ${pages.data.html_url || '-'}${pages.data.https_enforced ? ', HTTPS enforced' : ''}.`, 'note'));
  if (r.owner.login.toLowerCase() === 'sovereignwebsite') {
    box.append(el('p', 'This repository belongs to the SovereignWebsite organisation, which is run as code by SovereignWebsite__Factory. Change it there, not here.', 'note'));
  }
}

$('#signin').addEventListener('submit', e => {
  e.preventDefault();
  token = $('#token').value.trim();
  $('#token').value = '';
  if (!/^(github_pat_|ghp_|gho_|ghu_)[A-Za-z0-9_]+$/.test(token)) { $('#status').textContent = 'That does not look like a GitHub token.'; token = ''; return; }
  $('#forget').hidden = false;
  overview();
});
$('#forget').addEventListener('click', () => {
  token = '';
  $('#out').textContent = ''; $('#detail').textContent = ''; $('#rate').textContent = '';
  $('#status').textContent = 'Token forgotten. Nothing was stored.';
  $('#forget').hidden = true;
});
