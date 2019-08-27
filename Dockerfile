# As Scrapy runs on Python, I choose the official Python 3 Docker image.
FROM python:3

# Set the working directory to /tmp/src/
#WORKDIR /tmp/src/

# Copy the file from the local host to the filesystem of the container at the working directory.
COPY requirements.txt ./

# Install Scrapy specified in requirements.txt.
RUN pip3 install --no-cache-dir -r requirements.txt

# Download Spacy NLP model
# RUN python -m spacy download en_core_web_sm

# Expose port 6800 for Scrapyd
EXPOSE 6800

# Copy the project source code from the local host to the filesystem of the container at the working directory.
COPY . .

RUN pwd && ls

#make startup script executable
RUN chmod 777 ./scripts/startup.sh

# Run the crawler when the container launches.  Sleep so script won't exit and container stays up
CMD ./scripts/startup.sh  ; sleep infinity
