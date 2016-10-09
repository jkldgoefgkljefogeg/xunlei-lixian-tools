use dig to validate DNS record then add valid records to Smokeping Target
convert valid FQDNs from `dig -f +noall +answer` to SmokePing targets

## example input format
```dl.t6.lixian.vip.xunlei.com. 1783 IN	CNAME	t0540.sandai.net.
t0540.sandai.net.	1783	IN	A	61.147.76.41
dl.t13.lixian.vip.xunlei.com. 1785 IN	CNAME	t30a14.sandai.net.
t30a14.sandai.net.	1785	IN	A	180.153.91.143```

## Usage
`python3 smokeping-target-generator.py dig_output.txt target_output.txt`