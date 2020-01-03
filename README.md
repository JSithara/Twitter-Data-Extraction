# Twitter-Data-Extraction

**Cloud set up steps**:
a. An account was created with https://aws.amazon.com/ [1].

b. The virtual machine was launched with EC2.

c. A database instance was created; storage was added, and the security group was configured.

d. A new key pair was created and the key pair was downloaded(.pem_key)

e. The. pem key was loaded and the new paraphrase was created.

f. Both the public and private key was saved.

g. Putty config was opened, and public DNS was copied into it.

h. The .ppk file was attached under connection(ssh->auth) and clicked open.

i. On the command prompt, the username(ubuntu) and password were entered.

j. On successful cloud set up mongo db and apache spark was installed.

**Data extraction Process**:
For accomplishing the tweet extraction, a new twitter account has been created and that account
was used to create twitter app, from which the consumer and API keys were obtained[2] . Once
that was done, the tweepy was installed and the tweets were extracted using tweepy API. The
tweets were filtered according to various terms such as Canada, Canada Import, Canada
Export, Canada, Canada vehicle sales

**Data Cleaning**:
For Data cleaning, pandas have been used. The unwanted columns have been dropped to keep
only the columns which could be significant to the tweet report. Regex commands proved to
be useful to clean out unwanted characteristics. 

**References**:
[1] Amazon Web Services, Inc. (2019). Amazon Web Services (AWS) - Cloud Computing Services. [online]
Available at: https://aws.amazon.com/ [Accessed 2 Jul. 2019].

[2] Developer.twitter.com. (2019). Developer. [online] Available at: https://developer.twitter.com/ [Accessed
3 Jul. 2019].

[3]Spark.apache.org. (2019). Examples | Apache Sp
