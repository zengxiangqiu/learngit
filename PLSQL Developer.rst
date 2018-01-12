PL/SQL Developer
================

下载
---- 

点击 `allround automations`_


安装
----

安装后运行msi安装包

** 常见错误 **

1. 缺失 Oracle OCI ， 需下载 `Oracle Instant Client`_  ,版本应与服务器一致


解压后设置以下3个环境参数，此处以windows系统为例


:code:`PATH` -需要包含Instant Client的根目录（oci.dll所在位置） 

:code:`TNS ADMIN` -需要指出tnsnames.ora所在位置的根目录 

:code:`NLS LANG` -为客户设定语言，区域和特征（未设置，可能会出现中文乱码）。

tnsnames.ora
::

    XXXX =
      (DESCRIPTION =
        (ADDRESS_LIST =
          (ADDRESS = (PROTOCOL = TCP)(HOST = IP )(PORT = 1522))
        )
        (CONNECT_DATA =
          (SERVICE_NAME = XXXX )
        )
      )
      
NLS LANG
::

    NLS LANG = SIMPLIFIED CHINESE_CHINA.ZHS16GBK

实践
----

这方面建议参考内置Help文档，主要看图表、报告、工程 。

.. _allround automations: https://www.allroundautomations.com/

.. _Oracle Instant Client: http://www.oracle.com/technetwork/database/features/instant-client/index-097480.html



