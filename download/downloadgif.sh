string="url"  
urls=`curl -s ${string} | egrep -o 'http://\S*(\.gif)'`
echo ${urls} | awk 'BEGIN{FS = " "}{for (i=1;i<NF;i++) {if($i~/(url_host)/) {print $i}}}' >download.list
filepath='14'
mkdir ${filepath}
wget -P ${filepath} -i download.list 
# echo $url_name

