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
####26、getattr(object,name[,default])
返回一个对象的属性值                
**参数**                 
object -- 对象                        
name -- 字符串， 对象属性                           
default -- 默认返回值，如果不提供在没有对应属性时，将触发AttributeError              
**返回值**                      
返回对象属性值                              
####27、globals()              
以字典类型返回当前位置的全部全局变量              
**参数**         
无                            
**返回值**             
全局变量的字典             
####28、hasattr(object, name)
判断对象是否包含对应的属性                  
**参数**                                
object -- 对象                           
name -- 字符串， 属性名                      
**返回值**                      
如果对象有该属性则返回true，否则返回false
####29、hash(object)
获取一个对象(字符串或数值等)的哈希值             
**参数**
object -- 对象                    
**返回值**                            
对象的哈希值                                    
####30、help([object])
用于查看函数或模块用途的详细说明                     
**参数**                      
object -- 对象                                  
**返回值**                              
对象的帮助信息
####31、hex(x)
用于将10进制整数转换成16进制，并以字符串形式表示          
**参数**                  
x -- 10进制整数                           
**返回值**                     
以字符串表示的16进制             
####32、id(object)
获取对象的内存地址               
**参数**                     
object -- 对象                           
**返回值**                        
对象的内存地址
####33、input([prompt])
相当于eval(raw_input(prompt)),用来获取控制台的输入。                          
raw_input()将所有输入作为字符串看待，返回字符串类型；                                   
input()在对待纯数字输入时具有自己的特性，它返回输入的数字的类型(int ,float)                
####34、int(x, base=10)
将一个字符串或数字转换成整型                
**参数**                               
x -- 字符串或数字                         
base -- 进制数，默认为10进制                                 
**返回值**                            
返回整型数据
####35、isinstance(object, classinfo)
判断一个对象是否是一个已知的类型，类似type()                       
type()不会认为子类是一种父类类型，不考虑继承关系；                           
isinstance()会认为子类时一种父类，考虑继承关系；                   
如果要判断两个类型是否相同推荐使用isinstance()                              
**参数**              
object -- 实例对象                      
classinfo -- 可以是直接或间接类名，基本类型或者它们组成的元组                         
**返回值**                                        
如果对象的类型与参数二的类型相同则返回true,否则返回False
####36、issubclass(class, classinfo)
用于判断参数class是否是参数classinfo的子类                            
**参数**                      
class -- 类                                 
classinfo -- 类                             
**返回值**                             
如果class是classinfo的子类返回True，否则False
####37、iter(o[,sentinel])
生成迭代器                          
**参数**                 
o -- 支持迭代的集合对象                               
sentinel -- 如果传递了第二个参数，则参数object必须时一个可调用的对象，此时，iter创建了一个迭代器对象，每次调用这个迭代器对象的__next()__方法时，都会调用object               
**返回值**                            
迭代器对象
####38、len(s)
返回对象(字符、列表、元组等)长度或项目个数                             
**参数**                       
s -- 对象                        
**返回值**                              
对象长度 
####39、list([iterable])
将元组转换成列表                       
**参数**                     
iterable -- 要转换成列表的元组                              
**返回值**                           
转换成的列表
####40、locals()
以字典类型返回当前位置的全部局部变量
####41、long(x, base = 10)
将数字或字符串转换成一个长整型                   
**参数**                             
x -- 字符串或数字                       
base -- 可选，进制数，默认为10进制                              
**返回值**                                    
返回长整型
####42、map(function, iterable,...)
根据提供的函数对指定序列做映射。                                               
第一个参数function以参数序列中的每一个元素调用function函数，返回包含每次function函数返回值的新列表。                                      
**参数**                       
function -- 函数，有两个参数                            
iterable -- 一个或多个序列                               
**返回值**                                    
返回列表
####43、 max(iterable[, key])
####　　max(arg1, arg2, *args[, key])
* 取传入的多个参数中的最大值，或者传入的可迭代对象元素中的最大值。默认数值型参数，取最大值；字符型参数，取字母表排序靠后者。还可以传入命名参数Key,其为一个函数，用来指定取最大值的方法。‘’
* 至少传入两个参数，但是有只传入一个参数的例外，此时参数必须为可迭代对象，返回的是可迭代对象中的最大元素。
* 当存在多个相同的最大值时，返回的是最先出现的那个最大值
####44、memoryview(obj)
返回给定参数的内存查看对象，所谓内存查看对象，是指对支持缓冲区协议的数据进行包装，在不需要复制对象基础上允许Python代码访问。                        
**参数**                  
obj -- 对象                                       
**返回值**                                      
元组列表                                 
####45、min(iterable[,key])
####　　min(arg1, arg2, *args[, key])
* 取传入的多个参数中的最小值，或者传入的可迭代对象元素中的最小值。默认数值型参数，取最小值；字符型参数取字母表排序靠前者；还可以传入命名参数key，其为一个函数，用来指定取最小值的方法；
* 至少传入两个参数，但是有只传入一个参数的例外，此时参数必须为可迭代对象； 
####45、next(iterable[, default])
返回迭代器的下一个项目                       
**参数**               
iterable -- 可迭代对象                         
default -- 可选，用于设置在没有下一个元素时返回该默认值             
**返回值**                       
迭代器下一个项目              
####46、oct(x)
将一个整数转换成8进制的字符串                                         
**参数**                    
x -- 整数                               
**返回值**                                 
8进制字符串              
####47、open(name[, mode[, buffering]])
打开一个文件，创建一个file对象                     
**参数**                    
name -- 一个包含了你要访问的文件名称的字符串                      
mode -- 打开文件的模式，只读、写入、追加                       
buffering -- 如果buffering的值被设为0，就不会有寄存，如果值大于1，表明寄存区的缓冲大小                               
**返回值**                    
file对象                           
####48、ord(c)
ord()函数是chr()函数或unichr()函数的配对函数，它以一个字符作为参数，返回对应的ascii码                
**参数**                    
c -- 字符                         
**返回值**                     
对应参数的acsii码
####49、pow(x, y[, z])
计算x的y次方，如果z存在，则再对结果进行取模                        
**参数**                 
x -- 数值表达式                      
y -- 数值表达式                                    
z -- 数值表达式                                         
**返回值**                                            
返回x的y次方的值
####50、print(*objects, sep='', end='\n', file=sys.stdout)
用于打印输出                  
**参数**                             
objects -- 复数，表示可以一次输出多个对象，输出多个对象时，需要用分隔                         
sep -- 用来间隔多个对象，默认是一个空格                        
end -- 用来设定以什么结尾，默认是换行符'\n'                       
file -- 要写入的文件对象                              
**返回值**                     
无
####51、property([fget[, fset[, fdel[, doc]]]])
在新式类中返回属性值                       
**参数**                                 
fget -- 获取属性值的函数                     
fset -- 设置属性值的函数                           
fdel -- 删除属性值函数                                   
doc -- 属性描述信息                                   
**返回值**                                
新式类属性    
####52、range(stop)
####　　range(start, stop[, step])
创建一个整数列表，一般用在for循环中                            
**参数**                  
start -- 计数从start开始。默认从0开始。                              
stop -- 计数到stop结束，但不包括stop。                                    
step -- 步长，默认为1 

####53、raw_input([prompt])
用来获取控制台的输入。raw_input()将所有输入作为字符串看待，返回字符串类型               
####54、reduce(funtion, iterable[, initializer])
对参数序列中元素进行累积.用传给reduce中的函数function（有两个参数）先对集合中的第1、2个元素进行操作，得到的结果在与第三个数据用fucntion运算，最后得到一个结果。                  
**参数**                             
function -- 函数，有两个参数                       
iterable -- 可迭代对象                     
initializer -- 可选，初始参数                      
**返回值**                                       
返回函数计算结果
####55、reload(module)
从新载入之前载入的模块                               
**参数**                          
module -- 模块对象
####56、repr(object)
将对象转化为供解释器读取的对象             
**参数**                     
object -- 对象                              
**返回值**                           
一个对象的string格式
####57、reversed()
用于反向列表中元素         
####58、round(x [, n])
返回浮点数的四舍五入值                          
**参数**                   
x -- 数值表达式                             
n -- 数值表达式                   
**返回值**                        
返回浮点数的四舍五入值
####59、set([iterable])
创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集，差集，并集等。                  
**参数**                  
iterable -- 可迭代对象                                 
**返回值**                                
新的集合对象
####60、setattr(object, name, value)
设置属性值，该属性必须存在                         
**参数**                                
object -- 对象                      
name -- 字符串，对象属性                        
value -- 属性值                     
**返回值**                              
无
####61、slice(stop)
####　　slice(start, stop[, step])
实现切片对象，主要用在切片操作函数里的参数传递                        
**参数**                                
start -- 起始位置                           
stop -- 结束位置                             
step -- 间距                                    
**返回值**                              
一个切片对象
####62、sorted(iterable[, cmp[, key[, reverse]]])
对所以可迭代对象进行排序操作                                      
**参数**                       
iterable -- 可迭代对象                            
cmp -- 比较函数                             
key -- 主要用来比较的元素                         
reverse -- 排序规则， True- 降序； False - 升序                                
**返回值**                                                 
重新排序的列表