# #0014 graphify agents install matches the owned AGENTS H2 case-sensitively, so an existing  section is preserved and a duplicate lowercase  section is appended.

- 2026-06-30T21:00:21Z `issue`: graphify agents install matches the owned AGENTS H2 case-sensitively, so an existing  section is preserved and a duplicate lowercase  section is appended. [graphify/__main__.py:598; /home/jefferson/Dev/projetos/geral/youtube-content-extractor/AGENTS.md]
- 2026-06-30T21:02:46Z `attempt`: Made owned-section detection case-insensitive and added an uppercase-heading regression; 116 focused tests, skillgen, and 2549 full tests passed. [graphify/__main__.py:598] (worked)
- 2026-06-30T21:02:46Z `fix`: graphify agents install now adopts case variants such as  instead of appending a duplicate lowercase section. [graphify/__main__.py:598]
