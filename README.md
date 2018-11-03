资产采集
    方案一：SSH paramiko实现（中控机，agent装ssh服务器，适用于agent集齐比较少的）
     -fabric
     -ansible(内部就是paramiko模块，实现ssh连接)

    方案二saltstack(python开发的)批量操作首选，比ssh速度快
        -master（服务端）
          yum install salt-master
        -slave(奴隶，客户端)
           yum install salt-minion
           配置：master:1.1.1.1(master的ip)

         在master接受slave，授权
         master上执行subproess.getoutput('salt "*" cmd.run '执行命令') *表示接受的所有slave

    方案三agent(服务器多的时候，因为ssh连接耗时)
        v = subprocess.getoutput('ls')执行命令
        API：Django接收数据并入库

反射 getattr（）
导入字符串类型的模块impolib
目录
    -src业务
    -config自定义配置
    -bin启动
    -lib公共类库(包含内置配置)