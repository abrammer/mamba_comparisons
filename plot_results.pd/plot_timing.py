from zipfile import ZipFile
import matplotlib.pyplot as plt
import pandas as pd

archive = ZipFile('artifact.zip', 'r')
files = archive.namelist()

def extract_install_time(lines):
    penult_line = lines.splitlines()[-2]
    return float(penult_line.split()[-1][:-1])

data = {name.replace('.txt',''): extract_install_time(archive.read(name)) for name in archive.namelist()}
df = pd.Series(data)
df.index = df.index.str.split('_', expand=True)
df = df.reset_index()

for env, group in df.groupby('level_1'):
    fig, ax  = plt.subplots()
    group = group.set_index('level_0')
    group.plot.barh(ax=ax, rot=45, fontsize=9, title=env, legend=False,)
    ax.set_xlabel('seconds')
    ax.bar_label(ax.containers[0], fmt="%.0f")
    fig.savefig(f'{env}_timings.png')

for env, group in df.groupby('level_1'):
    fig, ax  = plt.subplots()
    group = group.set_index('level_0').drop('level_1', axis='columns')
    group /= group.loc['miniconda']
    group.plot.barh(ax=ax, rot=45, fontsize=9, title=env, legend=False,)
    ax.set_xlabel('seconds')
    ax.bar_label(ax.containers[0], fmt="%.0f")
    fig.savefig(f'{env}_timings_normalized.png')


fig, ax  = plt.subplots()
df['rank'] = df.groupby('level_1')[0].rank()
results = df.groupby('level_0')['rank'].mean()
results.plot.barh(ax=ax, rot=45, fontsize=9, title='Overall Ranking')
ax.bar_label(ax.containers[0], fmt="%.0f")
fig.savefig(f"Overall Ranking")
