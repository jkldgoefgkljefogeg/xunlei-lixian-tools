# use dig to validate DNS record then add valid records to Smokeping Target
# convert valid FQDNs from `dig -f +noall +answer` to SmokePing targets
#
# example input format
# dl.t6.lixian.vip.xunlei.com. 1783 IN	CNAME	t0540.sandai.net.
# t0540.sandai.net.	1783	IN	A	61.147.76.41
# dl.t13.lixian.vip.xunlei.com. 1785 IN	CNAME	t30a14.sandai.net.
# t30a14.sandai.net.	1785	IN	A	180.153.91.143
#
# Usage
# python3 smokeping-target-generator.py dig_output.txt target_output.txt
#
# 20161009
#
# To do
# update/replace on Target file
# customized node description
# make it more extensible/useable for other DNS records

import sys,logging,re
from more_itertools import unique_everseen

logging.basicConfig(level=logging.DEBUG)


def read_dig_output(filename:str) -> str:
    """convert dig output text file to string
    #
    """
    file_dig_output = open(filename, 'r')
    dig_output = file_dig_output.read()
    file_dig_output.close()
    logging.debug('dig_output: \n%s', dig_output)
    return dig_output


def get_cdn_nodes(string_dig_output:str)->list:
    """use regex to match URL pattern, put unique nodes into list of
    dict {'nodename':'t6', 'fqdn':'dl.t6.lixian.vip.xunlei.com.'}
    """
    list_nodes = []
    list_nodes_raw = list(unique_everseen(re.findall(r'dl\.\w+\.lixian\.vip\.xunlei\.com', string_dig_output)))
    for node_entry in list_nodes_raw:
        list_nodes.append({'node_name':re.search(r'dl\.(\w+)\.lixian\.vip\.xunlei\.com',node_entry).group(1),
                           'fqdn':node_entry})
    print(len(list_nodes), 'nodes found', )
    return list_nodes


def generate_target(cdn_nodes:list)->str:
    """generate SmokePing Target configuration block"""
    string_target = '''+ Xunlei_lixian
menu = Xunelei lixian
title = Xunlei lixian CDN nodes\n\n'''
    for cdn_nodes_entry in cdn_nodes:
        target_block_template = '''++ {0}
menu = {0}
title = Xunlei lixian CDN node {0}
host = {1}\n\n'''

        target_block=target_block_template.format(cdn_nodes_entry['node_name'], cdn_nodes_entry['fqdn'])
        logging.debug('target_block:\n%s',target_block)
        string_target += target_block
    return string_target


def write_target(path_target:str, string_target:str):
    """write Target config block to file"""
    file_target_output = open(path_target, 'w')
    file_target_output.write(string_target)
    file_target_output.close()


if __name__=='__main__':
    """
    """
    write_target(sys.argv[2], generate_target(get_cdn_nodes(read_dig_output(sys.argv[1]))))