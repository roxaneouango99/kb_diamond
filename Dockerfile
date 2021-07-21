FROM kbase/sdkbase2:python
MAINTAINER KBase Developer
# -----------------------------------------
# In this section, you can install any system dependencies required
# to run your App.  For instance, you could place an apt-get update or
# install line here, a git checkout to download code, or run any other
# installation scripts.

# RUN apt-get update
RUN \
    apt-get update && \
    apt-get -y install gcc
# The packages below are required for compiling diamond
RUN apt-get install wget
RUN apt-get install --yes cmake
RUN apt-get install --yes build-essential
RUN apt-get install --yes zlib1g-dev
RUN wget http://github.com/bbuchfink/diamond/archive/v2.0.4.tar.gz && \
    tar xzf v2.0.4.tar.gz && \
    cd diamond-2.0.4 && \
    mkdir bin && \
    cd bin && \
    cmake -DCMAKE_BUILD_MARCH=native .. && \
    make -j4 && \
    make install

# -----------------------------------------

COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod -R a+rw /kb/module

WORKDIR /kb/module

RUN make all

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
