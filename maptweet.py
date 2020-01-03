querys = ["oil","vehicle","university","dalhousie","expensive","good school","good schools","bad school","bad schools","poor school","poor schools","population","bus","buses","agriculture","economy" ]
for query in querys:
    text_file = sc.textFile("tweetlatest.txt")
    counts = text_file.flatMap(lambda line: line.split(" ")) \
                .map(lambda query: (query, 1)) \
                .reduceByKey(lambda a, b: a + b)
    print(counts.collect())


# querys = ["oil","vehicle","university","dalhousie","expensive","good school","good schools","bad school","bad schools","poor school","poor schools","population","bus","buses","agriculture","economy" ]
# for query in querys:
#     text_file = sc.textFile("tweetlatest.txt")
#     counts = text_file.flatMap(lambda line: line.split(" ")) \
#                 .map(lambda query: (query, 1)) \
#                 .reduceByKey(lambda a, b: a + b)
#     counts.saveAsTextFile("output/tweets")