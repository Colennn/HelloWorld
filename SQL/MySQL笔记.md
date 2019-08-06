# MySQL笔记



[TOC]



## 基本语句

```mysql
//创建表
Create Table table_name
(column_name1 column_type1,……)

//查询
Select column_name, column_name
From table_name
Where Clause

//插入
Insert Into table_name(field1, filed2, ……)
Values (value1, values2, ……)

//修改
Update table_name 
Set field1=new-value1, field=new-value2
Where Clause

//删除
Delete From table_name
Where Clause

```



## Group By

Group By 语句根据一个或多个列对结果集进行分组

在分组的列上我们可以使用Count、sum、avg等函数

```mysql
SELECT column_name, function(column_name)
FROM table_name
WHERE column_name operator value
GROUP BY column_name;

SELECT name, COUNT(*) FROM   employee_tbl GROUP BY name;
```





## 连接使用 Inner Join 、Left Join、Right Join 

统一公式：

```mysql
Select a.字段一, b.字段二，……
From 表一 a
Inner Join 表二 b
On a.字段一 = b.字段二
```

```mysql
Select a.rid, a.rauthor, b.rcount
From rtable a
Inner Join ttable b
On a.rauthor = b.rauthor
```

```mysql
Select a.rid, a.rauthor, b.rcount
From rtable a
Left Join ttable b
On a.rauthor = b.rauthor
```

```mysql
Select a.rid, a.rauthor, b.rcount
From rtable a
Right Join ttable b
On a.rauthor = b.rauthor
```


## 统计

```mysql
Select column_name, function(column_name)
From table_name
Where column_name operator value
Group By column_name
With Rollup;
```

function有三种：1.count()    2.sum()    3.avg()





## 必须要用‘Is Null‘或’Is Not Null‘  , 因为’= Null‘和’!= Null‘是不起作用的



## RegExp 正则表达式

```mysql
Select name
From tablename
Where name
REGEXP '^st'  //匹配以st开头的字符串
```

| 模式         | 描述                                       |
| ---------- | ---------------------------------------- |
| ^          | 匹配输入字符串的开始位置。如果设置了 RegExp 对象的 Multiline 属性，^ 也匹配 '\n' 或 '\r' 之后的位置。 |
| $          | 匹配输入字符串的结束位置。如果设置了RegExp 对象的 Multiline 属性，$ 也匹配 '\n' 或 '\r' 之前的位置。 |
| .          | 匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。 |
| [...]      | 字符集合。匹配所包含的任意一个字符。例如， '[abc]' 可以匹配 "plain" 中的 'a'。 |
| [^...]     | 负值字符集合。匹配未包含的任意字符。例如， '[ ^abc]' 可以匹配 "plain" 中的'p'。 |
| p1\|p2\|p3 | 匹配 p1 或 p2 或 p3。例如，'z\|food' 能匹配 "z" 或 "food"。'(z\|f)ood' 则匹配 "zood" 或 "food"。 |
| *          | 匹配前面的子表达式零次或多次。例如，zo* 能匹配 "z" 以及 "zoo"。* 等价于{0,}。 |
| +          | 匹配前面的子表达式一次或多次。例如，'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 {1,}。 |
| {n}        | n 是一个非负整数。匹配确定的 n 次。例如，'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o。 |
| {n,m}      | m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次。 |



## MySQL事务的四个特性

原子性、一致性、隔离性、持久性

1. 原子性：指事务包含的所有操作要么全部成功，要么全部回滚，因此事务的操作成功就必须要完全应用到数据库，如果操作失败则不能对数据库有任何影响
2. 一致性：一致性是指事务必须是数据库从一个一致性状态变换到另一个一致性状态。也就是一个事务执行之前和执行之后都必须处于一致性状态。
3. 隔离性：多个用户访问数据库时，比如操作同一张表时，数据库为每一个用户开启的事务都不能被其他事务干扰，多个并发事务之间要相互隔离。
4. 持久性：指一个事务一旦被提交了，那么对数据库中的数据改变就是永久性的。




## Alter语句是用来修改表明、修改数据表字段





## 索引

单例索引：一个索引只包含一个列，一个表可有多个索引

组合索引：一个索引包含多个列



索引的优点：大大提高了查询速度。

索引的缺点：会降低更新表的速度，因为更新表时，MySQL不仅要保存数据，还要保存一下索引文件。



```mysql
//创建索引
Create INDEX indexName
On mytable(username(length));

//创建表的时候直接指定
Create Tbale mytable(
	Id int NOT NULL,
  	username VARCHAR(16) NOT NULL,
  	INDEX [indexName] (username(length))
);
```



```mysql
#(1)创建索引
CREATE UNIQUE INDEX indexName ON mytable(username(length)) ;

#(2)创建表的时候直接指定
CREATE TABLE mytable( 
	ID INT NOT NULL,  
	username VARCHAR(16) NOT NULL,  
	UNIQUE [indexName] (username(length))  
);
```



## 视图

```mysql
CREATE OR REPLACE VIEW view_name_1 AS 
SELECT r.* FROM tb_role r RIGHT JOIN tb_admin a ON a.id=r.create_id;
-- 视图更新有很多限制 比如说 带常量的查询 带limit的查询 带聚合函数的查询 子查询 等等 实际使用中自测一下就行了
```



## 存储过程

存储过程思想上很简单，就是数据SQL语言层面的代码封装与重用。

优点：

- 存储过程可以封装，并隐藏复杂的商业逻辑
- 存储过程可以回传值，并可以接收参数
- 存储过程无法使用Select指令来运行，因为它是子程序，与查看表，数据表或用户定义函数不同
- 存储过程可以用在数据校验，强制实行商业逻辑等

缺点：

- 存储过程，往往定制化与特定的数据库上，因为支持的编程语言不同。当切换到其他厂商的数据库系统时，需要重写原有的存储过程
- 存储过程的性能调校与撰写，受限于各种数据库系统。

```mysql
DROP procedure IF EXISTS 'getGameName'; #删除存储过程

#注意参数名不能与字段名相同  DELIMITER是定界符的意思
DELIMITER $$
CREATE PROCEDURE getGameName(
  IN gameid INT, #入参
  OUT g_name VARCHAR(45), #出参
  OUT pin_yin VARCHAR(45) #出参  
)
BEGIN
	SELECT ganename
	INTO g_name
	FROM cy_name
	WHERE id = gameid;
	
	SELECT pinyin
	INTO pin_yin
	FROM cy_game
	WHERE id = gameid;
END$$
DELIMITER;

```



## MySQL中实现rank排名查询

基本知识：

1. sql语句中，使用@来定义一个变量。如：@abc

2. sql语句中，使用:=来给变量赋值： @abc := 123，则变量abc值为123

3. sql语句中，if(A,B,C)表示，如果A条件成立，那么执行B，否则执行C，                                   如：@abc :=if(2>1,100,200)的结果是，abc的值为100。

4. @case…when…then语句

   case…when…then语句有两种情况：

   case情况一（CASE后面不带表达式）：

   ```mysql
   CASE WHEN expression THEN 操作1

              WHEN expression THEN 操作2

               .......

              ELSE 操作n

   END
   ```

   注：自上而下，凡是走了其中一个when或者else了，其他的都不再走了

   case情况二（CASE 后面带表达式，此时WHEN 后面的则是该表达式可能的值）：

   ```mysql
   CASE expression

   WHEN  expression的值1 THEN  操作1

   WHEN  expression的值2 THEN  操作2

        .......

       ELSE 操作n

   END
   ```

   ​



## 其他知识点链接

[mysql 基础教程 很全 -- CSDN](https://blog.csdn.net/qq_16024861/article/details/81912713)

[浅谈sql中的in与not in,exists与not exists的区别以及性能分析 -- CSDN](https://blog.csdn.net/baidu_37107022/article/details/77278381)

[SQL常用函数大全 -- 简书](https://www.jianshu.com/p/fc627da82bb9)

[SQL的IF用法](https://www.cnblogs.com/xuhaojun/p/9141396.html)

[MySQL实现rank排名查询](https://blog.csdn.net/justry_deng/article/details/80597916)

[MySQL varchar转int类型的方法](https://blog.csdn.net/qq_26599807/article/details/82012498)





