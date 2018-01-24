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