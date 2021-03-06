import sys
sys.path.append('../../../lib/dm/spider')
import urllib
from minisb import MiniSpider

retdir = '/data/health_doc/xywy'
seeds = ['http://www.xywy.com', 
		 'http://hxnk.xywy.com/fy/jc/20141023/955246.html',
		 'http://jib.xywy.com/il_sii_9900.htm?fromurl=xywyhomepage',
		 'http://healthshare.xywy.com/healthdetail/486821.htm',
		 'http://jib.xywy.com']
white_list = [r'http://\w+.xywy.com/\w+/\w+/\d+/\d+\.html', r'http://healthshare.xywy.com/healthdetail/\d+\.htm']
sb = MiniSpider('%s/db' % retdir, '%s/page' % retdir, seeds, 
		white_list = white_list, thread_num = 6, time_sleep = 0.1,
		queue_max_size = 1e6, url_max_size = 1e9, file_max_size = 1e12)

if sb.prepare():
	sb.run()

