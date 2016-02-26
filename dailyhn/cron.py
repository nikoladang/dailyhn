from django.utils import timezone
from datetime import datetime, timedelta
from dailyhn.views.entry_views import get_top_stories_single_day
from dailyhn.models import Entry


def entries_single_day_cron(aDate, story_count=10):
    print("entries_single_day_cron "+str(datetime.now()))
    dictResult = get_top_stories_single_day(aDate)
    hnDate = datetime.strptime(dictResult["hnDate"],"%Y-%m-%d")
    insertList = []
    for value in dictResult["hnValue"]:
        print(value["title"])
        insertList.append(Entry(
            date = hnDate,
            points=value["points"],
            title=value["title"],
            article_url=value["url"],
            comment_url="https://news.ycombinator.com/item?id="+value["objectID"],
        ))
    Entry.objects.bulk_create(insertList)
    return insertList


def daily_entry_cron():
    # print("entries_single_day_cron"+str(timezone.now()))
    print("daily_entry_cron "+str(datetime.now()))
    today = datetime.now()
    chosenDate = (today-timedelta(days=1))

    # entries_single_day_cron(curYear, curMonth, curDay-1, story_count=10)
    entries_single_day_cron(chosenDate, story_count=10)


# def daily_entry_cron2():
#     print("entries_single_day_cron"+str(timezone.now()))
#     today = datetime.now()
#     curYear = today.year
#     curMonth = today.month
#     curDay = today.day
#
#     dictResult = get_top_stories_single_day(curYear,curMonth,curDay-1, story_count=10)
#     hnDate = datetime.strptime(dictResult["hnDate"],"%Y-%m-%d")
#     insertList = []
#     for value in dictResult["hnValue"]:
#         print(value["title"])
#         insertList.append(Entry(
#             date = hnDate,
#             points=value["points"],
#             title=value["title"],
#             article_url=value["url"],
#             comment_url="https://news.ycombinator.com/item?id="+value["objectID"],
#         ))
#     Entry.objects.bulk_create(insertList)
#     print(type(hnDate))
#     return dictResult


# def entries_single_day_cron2():
#     hnDate = datetime.strptime("2011-11-11","%Y-%m-%d")
#     # e = Entry.objects.create(
#     #     date=date(2016, 1, 10),
#     #     points=100,
#     #     title="A Guide to Seed Fundraising",
#     #     article_url="http://themacro.com/articles/2016/01/how-to-raise-a-seed-round/",
#     #     comment_url="https://news.ycombinator.com/item?id=10868717",
#     # )
#
#     e = Entry.objects.create(
#         date=hnDate,
#         points=100,
#         title="A Guide to Seed Fundraising",
#         article_url="http://themacro.com/articles/2016/01/how-to-raise-a-seed-round/",
#         comment_url="https://news.ycombinator.com/item?id=10868717",
#     )
#     e.save()

