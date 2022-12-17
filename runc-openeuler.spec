#needsrootforbuild
%global _bindir /usr/bin
%global debug_package %{nil}

Name: docker-runc
Version: 1.0.0.rc3
Release: 308
Summary: runc is a CLI tool for spawning and running containers according to the OCI specification.

License: ASL 2.0
Source0: https://github.com/opencontainers/runc/archive/v1.0.0-rc3.zip
Source1: patch.tar.gz
Source2: apply-patch
Source3: series.conf
Source4: git-commit
Source5: gen-commit.sh 

URL: https://www.opencontainers.org/
Vendor: OCI
Packager: OCI

BuildRequires: golang >= 1.8.3 glibc-static make libseccomp-devel libseccomp-static libselinux-devel

%description
runc is a CLI tool for spawning and running containers according to the OCI specification.

%prep
cp %{SOURCE0} .
cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE3} .
cp %{SOURCE4} .

%install
sh ./apply-patch 

mkdir -p .gopath/src/github.com/opencontainers
export GOPATH=`pwd`/.gopath
ln -sf `pwd` .gopath/src/github.com/opencontainers/runc
cd .gopath/src/github.com/opencontainers/runc
export GO111MODULE=off
make BUILDTAGS="seccomp selinux" static 
rm -rf .gopath
strip runc

install -d $RPM_BUILD_ROOT/%{_bindir}
install -p -m 755 runc $RPM_BUILD_ROOT/%{_bindir}/runc

%clean
%{__rm} -rf %{_bindir}/runc

%files
%{_bindir}/runc

%changelog
* Sat Dec 17 2022 zhongjiawei<zhongjiawei1@huawei.com> - 1.0.0.rc3-308
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:support specify umask

* Thu Dec 15 2022 zhongjiawei<zhongjiawei1@huawei.com> - 1.0.0.rc3-307
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:support set cpuset.perfer

* Mon Nov 21 2022 Ge Wang <wangge20@h-partners.com> - 1.0.0.rc3-306
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:add errnoRet in Syscall struct

* Wed Sep 28 2022 zhongjiawei<zhongjiawei1@huawei.com> - 1.0.0.rc3-305
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:move install path to /usr/bin

* Thu Sep 22 2022 zhongjiawei<zhongjiawei1@huawei.com> - 1.0.0.rc3-304
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:add CGO security build option

* Tue Aug 16 2022 zhongjiawei<zhongjiawei1@huawei.com> - 1.0.0.rc3-303
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix systemd cgroup after memory type changed

* Tue Aug 9 2022 zhongjiawei<zhongjiawei1@huawei.com> - 1.0.0.rc3-302
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:change Uamsk to 0022

* Tue Aug 09 2022 zhongjiawei<zhongjiawei1@huawei.com> - 1.0.0.rc3-301
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:sync bugfix, include
       1. add check in spec
       2. add mount destination validation(fix CVE-2021-30465)
       3. fix backport patch apply ignored
       4. optimize nsexec logging
       5. improve log for debugging
       6. fix cgroup info print error
       7. fix CVE-2022-29162

* Thu Dec 23 2021 xiadanni<xiadanni1@huawei.com> - 1.0.0.rc3-114
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:disable go module build

* Wed Mar 18 2021 xiadanni<xiadanni1@huawei.com> - 1.0.0.rc3-113
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:do not use -i in go build

* Thu Mar 18 2021 xiadanni<xiadanni1@huawei.com> - 1.0.0.rc3-112
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:build security option

* Thu Mar 18 2021 xiadanni<xiadanni1@huawei.com> - 1.0.0.rc3-111
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:sync bugfix, include
       1. add cpu and memory info when print cgroup info
       2. fix freezing race

* Fri Dec 11 2020 yangyanchao <yangyanchao6@huawei.com> - 1.0.0.rc-110
- add symbol in sys to support riscv
