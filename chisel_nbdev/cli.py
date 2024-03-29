# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/06_cli.ipynb (unless otherwise specified).

__all__ = ['bump_version', 'nbdev_bump_version', 'nbdev_install_git_hooks', 'extract_tgz', 'nbdev_new']

# Cell
from nbdev.imports import *
from .export_scala import *
from .sync_scala import *
from nbdev.merge import *
from .export_scala2html import *
from .clean_scala import *
from .test_scala import *
from fastcore.script import *

# Cell
def bump_version(version, part=2):
    version = version.split('.')
    version[part] = str(int(version[part]) + 1)
    for i in range(part+1, 3): version[i] = '0'
    return '.'.join(version)

# Cell
@call_parse
def nbdev_bump_version(part:Param("Part of version to bump", int)=2):
    "Increment version in `settings.py` by one"
    cfg = Config()
    print(f'Old version: {cfg.version}')
    cfg.d['version'] = bump_version(Config().version, part)
    cfg.save()
    update_version()
    print(f'New version: {cfg.version}')

# Cell
@call_parse
def nbdev_install_git_hooks():
    "Install git hooks to clean/trust notebooks automatically"
    try: path = Config().config_file.parent
    except: path = Path.cwd()
    hook_path = path/'.git'/'hooks'
    fn = hook_path/'post-merge'
    hook_path.mkdir(parents=True, exist_ok=True)
    #Trust notebooks after merge
    fn.write_text("#!/bin/bash\necho 'Trusting notebooks'\nchisel_nbdev_trust_nbs")
    os.chmod(fn, os.stat(fn).st_mode | stat.S_IEXEC)
    #Clean notebooks on commit/diff
    (path/'.gitconfig').write_text("""# Generated by chisel_nbdev_install_git_hooks
#
# If you need to disable this instrumentation do:
#   git config --local --unset include.path
#
# To restore the filter
#   git config --local include.path .gitconfig
#
# If you see notebooks not stripped, checked the filters are applied in .gitattributes
#
[filter "clean-nbs"]
        clean = chisel_nbdev_clean_nbs --read_input_stream True
        smudge = cat
        required = true
[diff "ipynb"]
        textconv = chisel_nbdev_clean_nbs --disp True --fname
""")
    cmd = "git config --local include.path ../.gitconfig"
    print(f"Executing: {cmd}")
    run(cmd)
    print("Success: hooks are installed and repo's .gitconfig is now trusted")
    try: nb_path = Config().path("nbs_path")
    except: nb_path = Path.cwd()
    (nb_path/'.gitattributes').write_text("**/*.ipynb filter=clean-nbs\n**/*.ipynb diff=ipynb\n")

# Cell
_template_git_repo = "https://github.com/fastai/nbdev_template.git"

# Cell
import tarfile

# Cell
def extract_tgz(url, dest='.'):
    with urlopen(url) as u: tarfile.open(mode='r:gz', fileobj=u).extractall(dest)

# Cell
@call_parse
def nbdev_new():
    "Create a new nbdev project from the current git repo"
    url = run('git config --get remote.origin.url')
    if not url: raise Exception('This does not appear to be a cloned git directory with a remote')
    author = run('git config --get user.name').strip()
    email = run('git config --get user.email').strip()
    if not (author and email): raise Exception('User name and email not configured in git')

    # download and untar template, and optionally notebooks
    FILES_URL = 'https://files.fast.ai/files/'
    extract_tgz(f'{FILES_URL}nbdev_files.tgz')
    path = Path()
    for o in (path/'nbdev_files').ls():
        if not Path(f'./{o.name}').exists(): shutil.move(str(o), './')
    shutil.rmtree('nbdev_files')
    if first(path.glob('*.ipynb')): print("00_core.ipynb not downloaded since a notebook already exists.")
    else: urlsave(f'{FILES_URL}00_core.ipynb')
    if not (path/'index.ipynb').exists(): urlsave(f'{FILES_URL}index.ipynb')

    # auto-config settings.ini from git
    settings_path = Path('settings.ini')
    settings = settings_path.read_text()
    owner,repo = repo_details(url)
    branch = run('git symbolic-ref refs/remotes/origin/HEAD').strip().split('/')[-1]
    settings = settings.format(lib_name=repo, user=owner, author=author, author_email=email, branch=branch)
    settings_path.write_text(settings)

    nbdev_install_git_hooks()
    if not (path/'LICENSE').exists() and not (path/'LICENSE.md').exists():
        warnings.warn('No LICENSE file found - you will need one if you will create pypi or conda packages.')