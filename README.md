# url_shortner
Containerized url_shortner

<h2>Setting up application</h2>
<pre>
1. Clone the repositiry
   git clone
2. Traverse insede url-shortner directory
   cd url_shortner
3. Build docker image
   docker build -t url_shortner:latest .
4. Once the image build is complete you can verify using below command
  docker images
  output:
  REPOSITORY                              TAG             IMAGE ID       CREATED         SIZE
  url_shortner                            latest          d772fc233276   2 minutes ago   449MB
5. Run docker container from image
  docker run -p 5000:5000 url-shortner:latest
  output:
  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
  * Restarting with stat
  * Debugger is active!
  * Debugger PIN: 247-353-832
</pre>
<h2>using applicaion</h2>
<pre>
Run below api from the machine where the container is running
curl http://0.0.0.0:5000/url_shortner/url=<url>
  
  Example: curl http://0.0.0.0:5000/url_shortner/url=google.com 
</pre>

<h2> Testing </h2>
<pre>
Case1:
Description: if you just enter below URl it will describe what is this app and how to use
enter URL :  curl http://0.0.0.0:5000/
output:
</pre>
<pre>+++++++++Welcome to free URL shortening service+++++++++
         please enter below api call to shorten your URL
         curl http://0.0.0.0:5000/url_shortner/url=google.com </pre>
<pre>

Case2:
Description: pass on some URL and it return shortened URL
enter URL :  curl http://0.0.0.0:5000/url_shortner/url=yahoo.com
output:
</pre>
<pre> http://0.0.0.0:5000/xjmb38</pre>
<pre>
Case3:
Description: Re-enter the same URL
enter URL :  curl http://0.0.0.0:5000/url_shortner/url=yahoo.com
output:
</pre>
<pre>URL alraedy exists, the shortned URL is http://0.0.0.0:5000/xjmb38</pre>
<pre>
<b>Case4:</b>
Description: Error handling enter wrong url
enter url: curl http://0.0.0.0:5000/ur
output:
</pre>
<pre>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
</pre>



