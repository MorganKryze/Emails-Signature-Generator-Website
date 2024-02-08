echo "----- Creating translation ids -----"
python manage.py makemessages -l en
python manage.py makemessages -l fr
python manage.py makemessages -l es
python manage.py makemessages -l de
echo "----- Done -----"