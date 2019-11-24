# 1 准备rabbitmq
```centos7 安装准备rabbitmq

yum install epel-release
yum install rabbitmq-server
systemctl start rabbitmq-server
systemctl enable rabbitmq-server
rabbitmqctl add_user admin password
rabbitmqctl set_user_tags myuser administrator
rabbitmqctl add_vhost celery_vhost
rabbitmqctl set_permissions -p celery_vhost admin ".*"   ".*"   ".*"
rabbitmq-plugins enable rabbitmq_management
systemctl restart rabbitmq-server


http://ip:15672
```

# 2. 启动work
```angular2

cd /project/path
celery worker -A project -l info
```

# 3 启动调度器
```angular2
cd /project/path
celery -A project  beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```