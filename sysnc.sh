## ��ȡ����

sleep 1

git add .
echo "�����뱾�α�ע��Ϣ"
read message
git commit -m "$message" --no-verify
echo "��ʼ�ύ���롭��"
git push origin master

pid=$!

wait ${pid}

