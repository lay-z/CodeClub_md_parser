source venv/bin/activate

mkdir -p code_club
cd code_club
git init
git remote add origin https://github.com/CodeClub/scratch-curriculum.git
git pull --quiet
cd ..

python update_projects.py