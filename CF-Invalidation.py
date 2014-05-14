#/usr/bin/python
#########################################################################
#
#
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#-----------------------------------------------------------------------
#
# Author    : Nitheesh  <nitheeshp@outlook.com>
#
#-----------------------------------------------------------------------
#
# File: /home/ec2-user/cf-invalidate.py
#  
# This Python script read the objects path specified in invalid.txt and invalidates those objects

# and cleans the contents of invalid.txt


########################################################################


# Place your credntials placed your credentials in your $HOME/.boto

# Create file invalid.txt in the same script directory  and place your paths of objects to be invalidated

import boto
def main():
        distid = 'xxxxxxxxxx'
        invalidationfilepath = '/home/ec2-user/invalid.txt'
        paths  = open(invalidationfilepath,"r+")
        conn = boto.connect_cloudfront()
        inval_req = conn.create_invalidation_request(distid, paths)
        print inval_req
        touch = open(invalidationfilepath,"w")
        touch.write("")
main()

