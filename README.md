# url_shortner
Containerized url_shortner

<h2>Setting up application</h2>
<pre>
1. Clone the repositiry
  `git clone` 
2. Traverse insede url-shortner directory
  `cd url_shortner`
3. Build docker image
  `docker build -t url_shortner:latest .`
4. Once the image build is complete you can verify using below command
  `docker images`
  output:
  REPOSITORY                              TAG             IMAGE ID       CREATED         SIZE
  url_shortner                            latest          d772fc233276   2 minutes ago   449MB
5. Run docker container from image
  `docker run -p 5000:5000 url-shortner:latest`
</pre>
