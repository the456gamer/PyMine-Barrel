===========
 brainstorm
===========

data storage
============
* non-unique resource id, from resource's unique id from files like plugin.yml
   * search for resource based on this
* unique resource UUID that always refferences the resource possibly 8 digit case insensitve hex values (45B9E6B4)?
   * spigot uses sequential, numerical ids, but sequential is bad.
   * possibly 8 digit case insensitve hex values (45B9E6B4)?
   * check for bad/swear words on generation (add custom wordlist?)
   * check that the id is not in use
   * python3 -c "import secrets;print(secrets.token_hex(4))" can generate with secrets module? or similar
* unique authors
   * use alphanumeric usernames
* store resource details
   * Type (PyMine), add more handelers? (TAGS?)
   * verification status (pymine only)
   * upload 1 archive and it fetchs/obtains the required information
      * pymine -> unzip archive, open plugin.yml, read giturl, plugin name, etc
      * manually verified by a human
      * once approved, the hash (and other information about the file) is put into a json sidecar file, and  signed using the repositorys distributer certificate


API
===

needed routes
-------------
- create (project)
- upload (version)
- edit (project)
- edit (version)
- download (version)
- download (project)
- download (searchresults)
- search (projects)
- reviews -> responding to as author, making reviews is open to too much abuse.

Authentication
--------------
- users can apply for secret api key on profile?
- api key -> session token
- session token determines permissions in namespace
- when creating a session token, can choose permissions it has
- check total permissions of api key too
- differentiate between user perms and admin perms. user perms only in their own namespace
- admin perms in all namespaces
- use python decoraters ( ``@permissions.requireall(["permission.user.*"])`` )
 

projects
========

namespaces
----------

- user groups (like github organisations)
- orgs or users can be owners of projects
- orgs have members + owners
- users can add indivial members to have rember perms on their repositorys
- transfer around namespaces 
    - user -> organisations
    - organisations -> user
    - user -> user
    - organisations -> organisations
- organisations has can an api key directly in the namespace (rather than a user) -> looks like a shared account / bot account

information page
----------------
- description
- title
- subtitle (tagline)
- TAGS
   - catagory/admintools
   - usage/server
   - servertype/pymine
   - each tag should have information
      - like name
      - decription (hover text?)
      - colour (display like badges?)
- reviews/ratings
   - starts, 1-5
   - average incuding decimals
- changelog
- donation link
- source code link
- feedback link
- documentation link
- main website link
- issue link
- support link
- versioned files view + download all previous versions
- shows verification status
- visability -> make page hidden to non contibutors etc (sunsetting a plugin, editing description)
   - public
   - unlisted (if you have the link, you can see the plugin)
   - private (need to be contibutors to see plugin)
- dependancys