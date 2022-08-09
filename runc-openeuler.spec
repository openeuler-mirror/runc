%global _bindir /usr/local/bin

Name: docker-runc
Version: 1.0.0.rc3
Release: 205
Summary: runc is a CLI tool for spawning and running containers according to the OCI specification.

License: ASL 2.0
Source: %{name}.tar.gz
Provides: runc

URL: https://www.opencontainers.org/
Vendor: OCI
Packager: OCI

BuildRequires: golang >= 1.8.3 glibc-static make libseccomp-devel libseccomp-static libselinux-devel

%description
runc is a CLI tool for spawning and running containers according to the OCI specification.

%prep
%setup -c -n runc

%install
./apply-patch 

mkdir -p .gopath/src/github.com/opencontainers
export GOPATH=`pwd`/.gopath
ln -sf `pwd` .gopath/src/github.com/opencontainers/runc
cd .gopath/src/github.com/opencontainers/runc
make BUILDTAGS="seccomp selinux" static 
rm -rf .gopath

install -d $RPM_BUILD_ROOT/%{_bindir}
install -p -m 755 runc $RPM_BUILD_ROOT/%{_bindir}/runc

%clean
%{__rm} -rf %{_bindir}/runc

%files
%{_bindir}/runc

%changelog
* Tue Aug 9 2022 zhongjiawei<zhongjiawei1@huawei.com> - 1.0.0.rc3-205
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:change Uamsk to 0022

* Tue Aug 09 2022 zhongjiawei<zhongjiawei1@huawei.com> - 1.0.0.rc3-204
- Type:CVE
- CVE:CVE-2022-29162
- SUG:NA
- DESC:do not set inheritable capabilities

* Fri Aug 20 2021 wangqing <wangqing@uniontech.com> - 1.0.0.rc3-203
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:provides runc

* Mon Aug 09 2021 xiadanni<xiadanni1@huawei.com> - 1.0.0.rc3-202
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix systemd cgroup after memory type changed

* Thu Jun 03 2021 xiadanni<xiadanni1@huawei.com> - 1.0.0.rc3-201
- Type:CVE
- CVE:CVE-2021-30465
- SUG:NA
- DESC:add mount destination validation(fix CVE-2021-30465)

* Wed Feb 9 2021 xiadanni<xiadanni1@huawei.com> - 1.0.0.rc3-200
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:sync bugfix and bump version to 200, bugfix include
       1. add cpu and memory info when print cgroup info
       2. fix freezing race

* Wed Nov 25 2020 xiadanni<xiadanni1@huawei.com> - 1.0.0.rc3-104
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:don't deny all devices when update cgroup resource
       do not permit /proc mounts to non-directories
       fix permission denied

* Fri Mar 20 2020 xiadanni<xiadanni1@huawei.com> - 1.0.0.rc3-103
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:pass back the pid of runc:[1:CHILD] so we can wait on it

* Thu Mar 5 2020 xiadanni<xiadanni1@huawei.com> - 1.0.0.rc3-102
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fixes config.Namespaces is empty when accessed
       write freezer state after every state check
       may kill other process when container has been stopped
       fix cgroup hugetlb size prefix for kB
       check nil pointers in cgroup manager

* Wed Jan 1 2020 xiadanni<xiadanni1@huawei.com> - 1.0.0.rc3-101
- Type:requirement
- ID:NA 
- SUG:NA
- DESC:package init
