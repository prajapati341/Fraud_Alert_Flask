create table login
(
	username varchar(20),
	password varchar(20)
)


insert into login values('sanjay','1234')
insert into login values('risk','1234')

select * from login;

select * from login where username='sanjay' and password='asdfsaf'

select username,password from login where username='sanjay' and password='1234'

select Fraud_Found,Investigator,Risk_Team_Remarks from Fraud_Alert
where session_id=114728735




Fraud_Alert


alter table Fraud_alert
rename column Fraud_Found [Fraud Found];

select * from fraud_alert where [Fraud Found] is null order by session_id

update test.dbo.Fraud_Alert
set [Fraud Found] =null,Investigator = null,Risk_Team_Remarks = null
where session_id in (114729151,
114729005,
114729267)
114729420,
114729585,
114729741,
114730226,
114730307,
114730307,
114730369,
114730518,
114730605,
114730634,
114730737)



select * from  Fraud_Alert
where session_id in (114729420);

select * from fraud_alert where convert(date,sess_start_time)='2022-10-15' and [Fraud Found] is not null

update fraud_alert
set [Fraud Found] =null,Investigator = null,Risk_Team_Remarks = null
where sess_start_time>='2022-10-18 15:00:00.000';



select * from students;

drop table students;