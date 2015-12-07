LOGFILE=/home/ubuntu/.virtualenvs/lms/lms.log
ERRORFILE=/home/ubuntu/.virtualenvs/lms/error.log
 
LOGDIR=$(dirname $LOGFILE)
 
NUM_WORKERS=3

ADDRESS=0.0.0.0:8000
 
 # user/group to run as
  
 USER=ubuntu
 
 GROUP=ubuntu
 
 APPNAME=Tango
 
 source /home/ubuntu/django-virt/bin/activate
 
 test -d $LOGDIR || mkdir -p $LOGDIR
 
 exec gunicorn Tango.wsgi:application  -w $NUM_WORKERS \
   --bind=$ADDRESS \
   --user=$USER\
   --group=$GROUP
   --log-level=debug \
   --log-file=$LOGFILE 2>>$LOGFILE  1>>$ERRORFILE  &



