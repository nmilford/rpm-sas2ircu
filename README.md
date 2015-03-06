rpm-sas2ircu
============

An RPM spec file for the SAS-2 Integrated RAID Configuration Utility (SAS2IRCU).

To Build:

`sudo yum -y install rpmdevtools && rpmdev-setuptree`

`wget https://raw.github.com/nmilford/rpm-sas2ircu/master/sas2ircu.spec -O ~/rpmbuild/SPECS/sas2ircu.spec`

You'll have to get the binaries from:

http://www.lsi.com/downloads/Public/Host%20Bus%20Adapters/Host%20Bus%20Adapters%20Common%20Files/SAS_SATA_6G_P20/SAS2IRCU_P20.zip

By clicking through the EULA and placing it in ~/rpmbuild/SOURCES/SAS2IRCU_P20.zip

`rpmbuild -bb ~/rpmbuild/SPECS/sas2ircu.spec`
