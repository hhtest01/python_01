#2.导包
from loguru import logger
#3.打印一条日志
logger.info("hello world")

#输出不同日志级别，debug,info,warning,sunccess,error
logger.add("a.log",level="DEBUG")
logger.debug("这是一条debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")
#输出到文件：aad()
logger.add("a.log",format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {line} | {module} | {message}",level="DEBUG")
logger.debug("这是一条debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")

#使用插入参数的格式化：
logger.info("我的名字叫{},今天星期几{}","张三","一")
