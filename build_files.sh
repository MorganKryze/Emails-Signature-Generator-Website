echo "----- Build start -----"
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
npm i @vercel/analytics
echo "----- Done -----"