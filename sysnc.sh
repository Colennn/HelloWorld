## ��ȡ����

sleep 1

git add .
echo "�����뱾�α�ע��Ϣ"
read message
git commit -m "$message" --no-verify
echo "��ʼ��ȡ���롭��"
git pull origin master

pid=$!

wait ${pid}

##�ύ����

echo "��ʼ�ύ���롭��"
git push origin master

pid=$!

wait ${pid}

echo "5s��ر�"
sleep 1
echo "4s��ر�"
sleep 1
echo "3s��ر�"
sleep 1
echo "2s��ر�"
sleep 1
echo "1s��ر�"
sleep 1