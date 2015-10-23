mkdir -p code_club
cd code_club
git init
git remote add origin https://github.com/CodeClub/scratch-curriculum.git
git pull
cd ..

export PYTHON_ENV=production
python3 update_projects.py