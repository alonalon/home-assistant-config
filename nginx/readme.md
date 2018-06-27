```
$ sudo docker run -it --rm \
      --volume /home/alon/apps/home/nginx/certificates:/etc/letsencrypt \
      --volume /home/alon/apps/home/nginx/letsencrypt:/data/letsencrypt \
      certbot/certbot \
      certonly \
      --webroot --webroot-path=/data/letsencrypt \
      -d home.aronhafner.com
```