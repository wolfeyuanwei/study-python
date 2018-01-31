###python标准函数学习笔记
####一、内建函数
####1、abs()
求绝对值
####2、all(iterable)
如果iterable的所有元素不为0，False、或者iterable为空，all(iterable)返回True,否则返回False，函数等价于：                      
>def all(iterable):                
>　　for element in ierable:　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
>		if not element:　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
>　　　　　　return False　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
>　　return True
####3、any(iterable)
如果iterable的元素中有一个不为0，False，any(iterable)返回True，否则返回False.函数等价于：                                
>def any(iterable):                                      
>　　for element in iterable:                                         
>　　　　if element:                                                
>　　　　　　return False                         
>　　return True
####4、basestring()
basestring()方法是str和unicode的超类，也是抽象类，所以不能被调用和实例化，但可用来判断一个对象是否为str或unicode的实例。                                      
isinstance(obj, basestring)
####5、bin(x)
将一个整形数字转化成二进制字符串。              
* 如果参数x不是一个整数，则x必须定义一个\_\_index\_\_()方法，并且返回值必须为整数            
* 如果x不是整数则报错                
* 如果x定义了\_\_index\_\_()方法，但返回值不是整数，报错                     
* 如果x定义了\_\_index\_\_()方法，且返回值为整数，将\_\_index\_\_()返回值转换成二进制字符串
####6、bool()
返回值为True或者False.                           
* 如果参数缺省，则返回False                                    
* 传入布尔类型时，按原值返回                              
* 传入字符串时，空字符串返回False否则返回True                        
* 传入数值时，0返回False否则True                        
* 传入元组、列表、字典等对象时，元素个数为空返回False，否则True
####7、bytearray()
返回一个新的字节数组。                                
* 当三个参数都不传的时候，返回长度为0的字节数组                               
* 当source参数为整数时，返回这个整数所指定长度的空字节数组                           
* 当source参数为实现了buffer接口的object对象时，那么将使用只读方式将字节读取到字节数组后                    
* 当source参数是一个可迭代对象，那么这个迭代对象的元素都必须符合0<= x < 256
####8、callable(object)
用来检测对象是否能被调用                                       
* 颗调用对象在实际调用也可能调用失败，但是不可调用对象，调用肯定不成功                                  
* 类对象都是可被调用对象，类的实例对象是否颗调用对象，取决于类是否定义\_\_call\_\_方法                 
####9、chr(i)
返回当前整数对应的ascii字符    
####10、classmethod()
给类用的，使用该注解把类中的的函数定义成类方法 
####11、cmp(x, y)
比较两个对象，x、y，如果x<y返回负数，如果x=y返回0，如果x>y返回正数
####12、compile(source, filename, mode[, flags[,dont_inherit]])
将一个字符串编译为字节代码            
**参数**              
* source - 字符串或者(AST)对象                            
* filename - 代码文件名称，如果不时从文件读取代码则传递一些可辨认的值；                     
* mode - 指定编译代码的种类。可以指定exec, eval, single;                                
* flags - 变量作用域，局部命名空间，如果被提供，可以时任何映射对象；                       
* flags,donot_inherit - 用来控制编译源码时的标志；                    
**返回值**        
返回表达式执行结果              
####13、complex([real[, imag]])
创建一个值为real+image*j的复数或者转化一个字符串为复数。如果第一个参数为字符串，则不需要指定第二个参数。                    
**参数**
real - int, long, float或字符串;                  
image - int, long, float;                       
**返回值**                       
返回一个复数              
####14、delattr(object, name)
用于删除属性                            
**参数**               
object - 对象                                  
name - 必须时对象的属性                           
**返回值**                           
无                 
####15、dict(**kwarg)                       
####　　dict(mapping, **kwarg)                
####　　dict(iterable, **kwarg)
创建一个字典              
**参数**                       
**kwarg - 关键字              
mappint - 元素的容器                            
iterable - 可迭代对象                           
**返回值**                             
返回一个字典             
####16、dir(object)
不带参数时，返回当前范围内的变量，方法和定义的类型列表；带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__(),该方法将被调用。如果参数不包含__dir__()，该方法将最大限度收集参数信息。              
**参数**                 
object -- 对象、变量、类型。                  
**返回值**                 
参数的属性列表                
####17、divmod(a, b)
把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a//b, a%b)              
**参数**                
a -- 数字                         
b -- 数字                      
**返回值**                        
商和余数的元组                       
####18、enumerate(sequence, start = 0)
将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标，一般用在for循环中               
**参数**                        
sequence -- 一个序列、迭代器或其他支持迭代对象                 
start -- 下标起始位置                
**返回值**                
enumerate枚举对象            
####19、eval(expression[, globals[, locals]])
执行一个字符串表达式，并返回表达式的值                           
**参数**                         
expression -- 表达式                                   
globals -- 变量作业域，全局命名空间，如果被提供必须是一个字典对象                 
locals -- 变量作用域，局部命名空间，如果被提供可以是任何映射对象            
**返回值**                      
表达式计算结果                                
####20、execfile(filename[, globals[, locals]])
执行一个文件                   
**参数**               
filename -- 文件名                    
globals -- 变量作业域，全局命名空间，如果被提供必须是一个字典对象                      
locals -- 变量作用域，局部命名空间，如果被提供可以是任何映射对象                     
**返回值**                    
表达式执行结果              
####21、open(name[, mode[, buffering]])
用于创建一个file对象，它有一个别名open()                 
**参数**                 
name -- 文件名                         
mode -- 打开模式                                     
buffering -- 0 表示不缓冲；1 表示缓冲； 大于1为缓冲区大小                       
**返回值**                 
文件对象                            
####22、filter(function, iterable)
用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表                  
**参数**              
function -- 判断函数                
iterable -- 可迭代对象                     
**返回值**             
符合条件的列表                             
####23、float(x)  
将整数或字符串转换成浮点数                     
**参数**            
x -- 整数或字符串                 
**返回值**        
浮点数                      
####24、format(value[,format_spec])
字符串格式化                              
####25、frozenset([iterable])
返回一个冻结的集合，冻结后的集合不能添加或删除任何元素                        
**参数**                   
iterable -- 可迭代的对象，如列表、字典、元组等                        
**返回值**                        
新的frozenset对象，如果不提供任何参数，默认生成空集合
