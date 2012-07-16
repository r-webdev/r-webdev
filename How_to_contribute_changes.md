###In order to contribute a change to this site:
* Make a github account
* set up a <a href="https://github.com/r-webdev/r-webdev/fork_select">fork</a> of <a href="https://github.com/r-webdev/r-webdev/">this repository</a>
* Create and modify  .md files in order to edit the tables that are compiled to this site.
* build the site (if you can't get the site to build, send the pull request anyway, it's very easy to build the .md files once you're set up)
* send a pull request using the github GUI

### Tech details
** In order to build the site on your own (although not necessary for all pull requests)
* Please clone this repo into your home folder
* clone @chjj's markup node.js compiler <a href="https://github.com/chjj/marked.git">https://github.com/chjj/marked.git</a> also into your homefolder
* run make in ~/marked
* run 'make clean; make;' in ~/r-webdev
