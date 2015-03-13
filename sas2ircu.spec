# To Build:
#
# sudo yum -y install rpmdevtools && rpmdev-setuptree
#
# wget https://raw.github.com/nmilford/specfiles/master/sas2ircu/sas2ircu.spec -O ~/rpmbuild/SPECS/sas2ircu.spec
#
# You'll have to get the binaries from:
#
# http://www.lsi.com/downloads/Public/Host%20Bus%20Adapters/Host%20Bus%20Adapters%20Common%20Files/SAS_SATA_6G_P20/SAS2IRCU_P20.zip
#
# By clicking through the EULA and placing it in ~/rpmbuild/SOURCES/SAS2IRCU_P20.zip
#
# rpmbuild -bb ~/rpmbuild/SPECS/sas2ircu.spec

Name:      sas2ircu
Version:   15.0
Release:   1%{?dist}
Summary:   LSI Corporation SAS2 IR Configuration Utility
License:   Unknown
Group:     RAID
URL:       http://www.lsi.com/downloads/Public/Host%20Bus%20Adapters/Host%20Bus%20Adapters%20Common%20Files/SAS_SATA_6G_P20/SAS2IRCU_User_Guide.pdf
Source0:   http://www.lsi.com/downloads/Public/Host%20Bus%20Adapters/Host%20Bus%20Adapters%20Common%20Files/SAS_SATA_6G_P20/SAS2IRCU_P20.zip
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
LSI Corporation SAS2 IR Configuration Utility

%prep
rm -rf %{_builddir}/%{name}-%{version}
mkdir -p %{_builddir}/%{name}-%{version}
cd %{_builddir}/%{name}-%{version}
unzip %{SOURCE0}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
cp %{_builddir}/%{name}-%{version}/SAS2IRCU_P20/sas2ircu_linux_x86_rel/sas2ircu %{buildroot}/%{_sbindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
%attr(0755,root,root) %{_sbindir}/sas2ircu

%changelog
* Wed Mar 06 2015 Kilian Cavalotti <kilian@stanford.edu> - 20.0-1
- Updated to 20.0

* Wed Jan 11 2013 Nathan Milford <nathan@milford.io> - 15.0-1
- Updated to 15.0

* Wed Jul 25 2012 Harvard University FAS Research Computing <rchelp@fas.harvard.edu> - 0.2-1
- use %{_sbindir}

* Fri Jul 20 2012 Harvard University FAS Research Computing <rchelp@fas.harvard.edu> - 0.1-1
- Initial package
