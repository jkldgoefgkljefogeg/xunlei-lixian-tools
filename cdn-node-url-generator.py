# convert a gdl url to node load balancer URLs
#
# input
# http://gdl.lixian.vip.xunlei.com/download?
#
# output list of node load balancer url, optionally with hyperlink
# http://dl.t6.lixian.vip.xunlei.com/download?
# http://dl.t13.lixian.vip.xunlei.com/download?
#
# 20161010
#
# To do
# now load balancing is done by gdl.lixian.vip.xunlei.com (it has been this way for a while)
# node load balancer is no longer being used
# occasionally node load balancer returns HTTP 410 while a vod server redirected from gdl can serve the content
# need a better way to determine if a file can be served by a node than merely testing the node load balancer

import sys

cdn_list = [{'fqdn': 'dl.t6.lixian.vip.xunlei.com', 'node_name': 't6'}, {'fqdn': 'dl.t13.lixian.vip.xunlei.com', 'node_name': 't13'}, {'fqdn': 'dl.t14.lixian.vip.xunlei.com', 'node_name': 't14'}, {'fqdn': 'dl.t15.lixian.vip.xunlei.com', 'node_name': 't15'}, {'fqdn': 'dl.t16.lixian.vip.xunlei.com', 'node_name': 't16'}, {'fqdn': 'dl.t18.lixian.vip.xunlei.com', 'node_name': 't18'}, {'fqdn': 'dl.t19.lixian.vip.xunlei.com', 'node_name': 't19'}, {'fqdn': 'dl.t20.lixian.vip.xunlei.com', 'node_name': 't20'}, {'fqdn': 'dl.t21.lixian.vip.xunlei.com', 'node_name': 't21'}, {'fqdn': 'dl.t22.lixian.vip.xunlei.com', 'node_name': 't22'}, {'fqdn': 'dl.t23.lixian.vip.xunlei.com', 'node_name': 't23'}, {'fqdn': 'dl.t24.lixian.vip.xunlei.com', 'node_name': 't24'}, {'fqdn': 'dl.t25.lixian.vip.xunlei.com', 'node_name': 't25'}, {'fqdn': 'dl.t26.lixian.vip.xunlei.com', 'node_name': 't26'}, {'fqdn': 'dl.t27.lixian.vip.xunlei.com', 'node_name': 't27'}, {'fqdn': 'dl.t28.lixian.vip.xunlei.com', 'node_name': 't28'}, {'fqdn': 'dl.t29.lixian.vip.xunlei.com', 'node_name': 't29'}, {'fqdn': 'dl.t30.lixian.vip.xunlei.com', 'node_name': 't30'}, {'fqdn': 'dl.t31.lixian.vip.xunlei.com', 'node_name': 't31'}, {'fqdn': 'dl.t33.lixian.vip.xunlei.com', 'node_name': 't33'}, {'fqdn': 'dl.t34.lixian.vip.xunlei.com', 'node_name': 't34'}, {'fqdn': 'dl.t36.lixian.vip.xunlei.com', 'node_name': 't36'}, {'fqdn': 'dl.t37.lixian.vip.xunlei.com', 'node_name': 't37'}, {'fqdn': 'dl.t38.lixian.vip.xunlei.com', 'node_name': 't38'}, {'fqdn': 'dl.t39.lixian.vip.xunlei.com', 'node_name': 't39'}, {'fqdn': 'dl.c1.lixian.vip.xunlei.com', 'node_name': 'c1'}, {'fqdn': 'dl.c5.lixian.vip.xunlei.com', 'node_name': 'c5'}, {'fqdn': 'dl.c6.lixian.vip.xunlei.com', 'node_name': 'c6'}, {'fqdn': 'dl.c7.lixian.vip.xunlei.com', 'node_name': 'c7'}, {'fqdn': 'dl.c8.lixian.vip.xunlei.com', 'node_name': 'c8'}, {'fqdn': 'dl.c10.lixian.vip.xunlei.com', 'node_name': 'c10'}, {'fqdn': 'dl.c11.lixian.vip.xunlei.com', 'node_name': 'c11'}, {'fqdn': 'dl.c12.lixian.vip.xunlei.com', 'node_name': 'c12'}, {'fqdn': 'dl.c13.lixian.vip.xunlei.com', 'node_name': 'c13'}, {'fqdn': 'dl.c14.lixian.vip.xunlei.com', 'node_name': 'c14'}, {'fqdn': 'dl.c15.lixian.vip.xunlei.com', 'node_name': 'c15'}, {'fqdn': 'dl.c16.lixian.vip.xunlei.com', 'node_name': 'c16'}, {'fqdn': 'dl.c17.lixian.vip.xunlei.com', 'node_name': 'c17'}, {'fqdn': 'dl.c18.lixian.vip.xunlei.com', 'node_name': 'c18'}, {'fqdn': 'dl.c19.lixian.vip.xunlei.com', 'node_name': 'c19'}, {'fqdn': 'dl.c20.lixian.vip.xunlei.com', 'node_name': 'c20'}, {'fqdn': 'dl.c21.lixian.vip.xunlei.com', 'node_name': 'c21'}, {'fqdn': 'dl.c22.lixian.vip.xunlei.com', 'node_name': 'c22'}, {'fqdn': 'dl.c23.lixian.vip.xunlei.com', 'node_name': 'c23'}, {'fqdn': 'dl.c24.lixian.vip.xunlei.com', 'node_name': 'c24'}, {'fqdn': 'dl.c26.lixian.vip.xunlei.com', 'node_name': 'c26'}, {'fqdn': 'dl.g.lixian.vip.xunlei.com', 'node_name': 'g'}, {'fqdn': 'dl.h.lixian.vip.xunlei.com', 'node_name': 'h'}, {'fqdn': 'dl.i.lixian.vip.xunlei.com', 'node_name': 'i'}, {'fqdn': 'dl.u.lixian.vip.xunlei.com', 'node_name': 'u'}, {'fqdn': 'dl.u1.lixian.vip.xunlei.com', 'node_name': 'u1'}, {'fqdn': 'dl.u2.lixian.vip.xunlei.com', 'node_name': 'u2'}, {'fqdn': 'dl.u3.lixian.vip.xunlei.com', 'node_name': 'u3'}, {'fqdn': 'dl.twin.lixian.vip.xunlei.com', 'node_name': 'twin'}]


def generate_url(url_gdl:str)->str:
    """one URL per line"""
    string_url = ''
    for cdn_list_entry in cdn_list:
        string_url += (url_gdl.replace(r'gdl', r'dl.' + cdn_list_entry['node_name']) + '\n')
    return string_url


def generate_url_hyperlink(url_gdl:str)->str:
    """format in hyperlink"""
    string_url = ''
    for cdn_list_entry in cdn_list:
        string_url += '<a href="' + (url_gdl.replace(r'gdl', r'dl.' + cdn_list_entry['node_name']) + '">' + cdn_list_entry['node_name'] +'</a>\n')
    return string_url


def write_url_file(string_url:str, write_url_path:str):
    file_url_out = open(write_url_path,'w')
    file_url_out.write(string_url)
    file_url_out.close()


if __name__=='__main__':
    """
    """
    # write_url_file(generate_url(sys.argv[1]), sys.argv[2])
    write_url_file(generate_url_hyperlink(sys.argv[1]), sys.argv[2])

