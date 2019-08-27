# Hibernate入门学习

​	本文主要讲的是Hibernate的入门知识。

## 目录

* [Hibernate入门学习](#hibernate%E5%85%A5%E9%97%A8%E5%AD%A6%E4%B9%A0)
  * [什么是Hibernate？什么是ORM？](#%E4%BB%80%E4%B9%88%E6%98%AFhibernate%E4%BB%80%E4%B9%88%E6%98%AForm)
  * [Hibernate开发步骤](#hibernate%E5%BC%80%E5%8F%91%E6%AD%A5%E9%AA%A4)
  * [准备Hibernate环境](#%E5%87%86%E5%A4%87hibernate%E7%8E%AF%E5%A2%83)


## 什么是Hibernate？什么是ORM？


​	Hibernate是一个ORM框架（Object Relative DateBase Mapping），在Java对象与关系数据库之间建立某种映射，以实现直接存取Java对象。

## Hibernate开发步骤

![](pic/1.png)

1. 创建Hibernate配置文件  hibernate.cfg.xml

   ```java
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE hibernate-configuration PUBLIC
   		"-//Hibernate/Hibernate Configuration DTD 3.0//EN"
   		"http://hibernate.sourceforge.net/hibernate-configuration-3.0.dtd">
   <hibernate-configuration>
   	<session-factory>
       
   		<!-- 配置连接数据库的基本信息：驱动、数据库地址、账户、密码 -->
   		<property name="connection.username">root</property>
   		<property name="connection.password">1234</property>
   		<property name="connection.driver_class">com.mysql.jdbc.Driver</property>
   		<property name="connection.url">jdbc:mysql://localhost/hibernate</property>
   		
   		<!-- 配置 hibernate 的基本信息 -->
   		<!-- hibernate 所使用的数据库方言,告诉Hibernate用什么数据库、什么引擎 -->
   		<property name="dialect">org.hibernate.dialect.MySQLInnoDBDialect</property>		
   		
   		<!-- 执行操作时是否在控制台打印 SQL -->
   		<property name="show_sql">true</property>
   	
   		<!-- 是否对 SQL 进行格式化：方便阅读SQL -->
   		<property name="format_sql">true</property>
   	
   		<!-- 指定自动生成数据表的策略：自动生成数据表 -->
   		<property name="hbm2ddl.auto">update</property>
   		
   		<!-- 指定关联的 .hbm.xml 文件 -->
   		<mapping resource="com/atguigu/hibernate/helloworld/News.hbm.xml"/>
   	
   	</session-factory>

   </hibernate-configuration>
   ```

2. 创建持久化类


   ```java
      package com.atguigu.hibernate.helloworld;

      import java.sql.Blob;
      import java.util.Date;

      public class News {
      	
      	private Integer id;
      	private String title;
      	private String author;
        	private Date date;
        
      	public Integer getId() { 
      		return id;
      	}

      	public void setId(Integer id) {
      		this.id = id;
      	}

      	public String getTitle() {
      		return title;
      	}

      	public void setTitle(String title) {
      		this.title = title;
      	}

      	public String getAuthor() {
      		return author;
      	}

      	public void setAuthor(String author) {
      		this.author = author;
      	}

      	public Date getDate() {
      		return date;
      	}

      	public void setDate(Date date) {
      		this.date = date;
      	}

      	public News(String title, String author, Date date) {
      		super();
      		this.title = title;
      		this.author = author;
      		this.date = date;
      	}
      	
      	public News() {
      		// TODO Auto-generated constructor stub
      	}

      	@Override
      	public String toString() {
      		return "News [id=" + id + ", title=" + title + ", author=" + author
      				+ ", date=" + date + "]";
      	}
      	
      }
   ```

3. 创建对象--关系映射文件  *.hbm.xml

   ```java
   <?xml version="1.0"?>
   <!DOCTYPE hibernate-mapping PUBLIC "-//Hibernate/Hibernate Mapping DTD 3.0//EN"
   "http://hibernate.sourceforge.net/hibernate-mapping-3.0.dtd">

   <hibernate-mapping package="com.atguigu.hibernate.helloworld">

       <class name="News" table="NEWS" dynamic-insert="true">
       	
           <id name="id" type="java.lang.Integer">
               <column name="ID" />
               <!-- 指定主键的生成方式, native: 使用数据库本地方式 -->
               <generator class="native" />
           </id>
       
           <property name="title" not-null="true" unique="true"
           	index="news_index" length="50"
           	type="java.lang.String" column="TITLE" >
           </property>
           
           <property name="author" type="java.lang.String"
           	index="news_index">
               <column name="AUTHOR" />
           </property>
           
           <property name="date" type="date">
               <column name="DATE" />
           </property>
           
           <property name="desc" 
           	formula="(SELECT concat(title, ',', author) FROM NEWS n WHERE n.id = id)"></property>
   		
   		<property name="content">
   			<column name="CONTENT" sql-type="text"></column>
   		</property>
   		
   		<property name="picture" column="PICTURE" type="blob"></property>
   		
       </class>
       
   </hibernate-mapping>
   ```

4. 通过Hibernate API编写访问数据的代码

   ```java
   package com.atguigu.hibernate.helloworld;

   import java.sql.Date;

   import org.hibernate.Session;
   import org.hibernate.SessionFactory;
   import org.hibernate.Transaction;
   import org.hibernate.cfg.Configuration;
   import org.hibernate.service.ServiceRegistry;
   import org.hibernate.service.ServiceRegistryBuilder;
   import org.junit.Test;

   public class HibernateTest {

   	@Test
   	public void test() {
   		
   		System.out.println("test...");
   		
   		//1. 创建一个 SessionFactory 对象
   		SessionFactory sessionFactory = null;
   		
   		//1). 创建 Configuration 对象: 对应 hibernate 的基本配置信息和 对象关系映射信息
   		Configuration configuration = new Configuration().configure();
   		
   		//版本4.0 之前这样创建
   //		sessionFactory = configuration.buildSessionFactory();
   		
   		//2). 创建一个 ServiceRegistry 对象: hibernate 4.x 新添加的对象
   		//hibernate 的任何配置和服务都需要在该对象中注册后才能有效.
   		ServiceRegistry serviceRegistry = 
   				new ServiceRegistryBuilder().applySettings(configuration.getProperties())
   				                            .buildServiceRegistry();
   		
   		//3).
   		sessionFactory = configuration.buildSessionFactory(serviceRegistry);
   		
   		//2. 创建一个 Session 对象
   		Session session = sessionFactory.openSession();
   		
   		//3. 开启事务
   		Transaction transaction = session.beginTransaction();
   		
   		//4. 执行保存操作
   		News news = new News("Java12345", "ATGUIGU", new Date(new java.util.Date().getTime()));
   		session.save(news);
   		
   		//5. 提交事务 
   		transaction.commit();
   		
   		//6. 关闭 Session
   		session.close();
   		
   		//7. 关闭 SessionFactory 对象
   		sessionFactory.close();
   	}
   	
   }
   ```


## 准备Hibernate环境

- 导入Hibernate必须的jar包

![](pic/2.png)

- 导入数据库驱动的jar包

![](pic/3.png)

