#needsrootforbuild
%global _bindir /usr/local/bin
%global debug_package %{nil}

Name: docker-runc
Version: 1.0.0.rc3
Release: 115
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
export GO111MODULE=off
export GOPATH=`pwd`/.gopath
ln -sf `pwd` .gopath/src/github.com/opencontainers/runc
cd .gopath/src/github.com/opencontainers/runc
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
* Tue Jan 26 2022 songyanting <songyanting@huawei.com> - 1.0.0.rc3-115
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
       7. support unit test

* Tue Oct 26 2021 chenchen <chen_aka_jan@163.com> - 1.0.0.rc3-114
- change the spec file name to be the same as the repo name

* Thu Mar 18 2021 xiadanni<xiadanni1@huawei.com> - 1.0.0.rc3-113
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
