# Some suggestions 

1-- Settings.py/Templates location : ['templates'] is enough , 
    even if the master html is outside the APP(in the BASE_DIR) and the childs are inside the APP

2-- Venv & Requirements.txt **(I have created , No need to create again)**

3-- UI is great :smirk: :smirk:

4-- No need to do 'app.apps.AppConfig; like that , 
    because now in 'apps.py' there is only one class ('Appconfig') and its specific registration is happening only

5-- **Change the database to POSTGRES before doing anything (Can checkout my Github...Its  just a suggestion, But please change)**

6-- Run migrations everytime (I have done the initial 19 s),nor You cannot see the changes.But be aware about putting *null,blank,default* as attributes inside fields (Faced a lot trouble :expressionless: :expressionless:) , you can optimize migrations or flush the database (although some data remains for that you have to go to PSQL shell and have to remove total data by SQL commands)
    *For more migration related commands , just type (python manage.py)*


** Please don't mind anything !! As the name describes , these are purely my suggestion ,(Not even an advice!!) **
** Merging is also upon you **