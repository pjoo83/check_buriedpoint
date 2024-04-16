import time

from tools.read_json import parse_json_file
from tools.read_pandas import read_file
import json
from tools.read_get_log import logger
from tools.read_all_files import find_file


def point_lists():
    """

    :return:本地址为需要检测点的文件地址
    """
    point_file = read_file(r'../event_info.xlsx')
    point_list = point_file.values
    return point_list


#
def json_list(file):
    """

    :return:地址放导出的抓包文件
    """
    json_file = parse_json_file(file)
    # json_file = parse_json_file(r'D:\project\Airtest_Check_BuriedPoints\ios_request_files\iospublish.chlsj')

    return json_file


def check_tools(file):
    """

    :return: 内容检查
    """
    no_info_list = []
    r_info_list = []
    need_r_info = need_Points()[0]
    need_point = need_Points()[1]
    event_list = get_events(file)[0]
    for i in range(len(event_list)):
        events = event_list[i]['event']
        r_info = event_list[i]['event_extra']
        for p in range(len(need_point)):
            if events == need_point[p] and need_r_info[p] == 'no':
                if 'r_info' in event_list[i]['event_extra']:
                    logger.error(f"{events}不该含有r_info,但带有这个值{event_list[i]['event_extra'].get('r_info')}")
                else:
                    no_info_list.append(events)
            elif events == need_point[p] and need_r_info[p] == 'yes':
                if r_info == '':
                    logger.error(f"本埋点为{events},本次含有的r_info{r_info}"
                                 f"但值为空!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

                else:
                    r_info_list.append({events: r_info})

    if check_same_point(no_info_list):
        for i in check_same_point(no_info_list):
            logger.error(f"埋点{i}重复")
    if check_same_point(r_info_list):
        for i in check_same_point(r_info_list):
            logger.error(f"埋点{i}重复")
    leak_detection(file)
    # print(r_info_list)


# 查找没有的
def leak_detection(file):
    need_point1 = need_Points()[1]
    events = get_events(file)[1]
    for p in range(len(need_point1)):
        if need_point1[p] not in events:
            print(f'{need_point1[p]}丢失')
            logger.error(f'{need_point1[p]}丢失')


def get_events(file):
    """

    :return: 获取接口中得需要部分
    """
    event_list = []
    e_list = []
    for i in range(len(json_list(file))):
        data = json.loads(json_list(file)[i])
        events = data.get('events')[0]
        event_list.append(events)
        e_list.append(events['event'])

    return event_list, e_list


def need_Points():
    """
    :return: 获取需要的埋点
    """
    need_point_list = []
    need_r_info = []
    for point in point_lists():
        if "(pass)" not in point[0]:
            need_point_list.append(point[0])
            need_r_info.append(point[1])
    # print(need_point_list, need_r_info)
    return need_r_info, need_point_list


def check_same_point(point_list):
    """

    :param point_list:
    :return: 判断内容相同
    """
    same_list = []
    for h in range(len(point_list)):
        for z in range(h + 1, len(point_list)):
            if point_list[h] == point_list[z]:
                same_list.append(point_list[h])
    # for i in point_list:
    #     if point_list.count(i) >= 2:
    #         same_list.append(i)
    #         print(f"{i}出现的次次数{point_list.count(i)}")
    return same_list


# check_tools()

def get_all_file():
    file_list = find_file("../json_datas", include_str="an")
    # file_list = find_file("../ios_jsondata", include_str="2-2")

    return file_list


def start_check():
    for check in get_all_file():
        print(check)
        logger.debug("开始检测========================================")
        check_tools(check)


start_check()
