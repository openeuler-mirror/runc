%global _bindir /usr/bin
%global debug_package %{nil}

Name: docker-runc
Version: 1.1.3
Release: 14
Summary: runc is a CLI tool for spawning and running containers according to the OCI specification.

License: ASL 2.0
Source0: https://github.com/opencontainers/runc/archive/refs/tags/v1.1.3.tar.gz
Source1: apply-patch
Source2: series.conf
Source3: git-commit
Source4: gen-commit.sh
Source5: patch.tar.gz

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
cp %{SOURCE5} .


%install
sh ./apply-patch
%ifarch loongarch64
patch -p1 < %{_builddir}/patch/0034-SIGUNUSED-is-nolonger-support-for-loongarch.patch
patch -p1 < %{_builddir}/patch/0035-update-sys-to-v0.4.0-to-support-loong64.patch
%endif

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
* Mon Apr 3 2023 zhongjiawei<zhongjiawei1@huawei.com> - 1.1.3-14
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix rootless /sys/fs/cgroup mounts bug and Prohibit /proc and /sys to be symlinks

* Tue Mar 21 2023 zhongjiawei<zhongjiawei1@huawei.com> - 1.1.3-13
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:libcontainer: skip chown of /dev/null caused by fd redirection

* Thu Mar 16 2023 zhaozhen <zhaozhen@loongson.cn> - 1.1.3-12
- Type:feature
- CVE:NA
- SUG:NA
- DESC:Add loongarch64 support

* Thu Feb 9 2023 zhongjiawei<zhongjiawei1@huawei.com> - 1.1.3-11
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:make runc spec compatible 1.0.0.rc3

* Tue Jan 17 2023 zhongjiawei<zhongjiawei1@huawei.com> - 1.1.3-10
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:modify linuxcontainer starttime uint64 type tobe string

* Tue Jan 10 2023 zhongjiawei<zhongjiawei1@huawei.com> - 1.1.3-9
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:support specify umask

* Thu Jan 5 2023 zhongjiawei<zhongjiawei1@huawei.com> - 1.1.3-8
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:modify apply-patch path

* Sat Dec 17 2022 zhongjiawei<zhongjiawei1@huawei.com> - 1.1.3-7
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:support specify umask

* Mon Nov 7 2022 zhongjiawei<zhongjiawei1@huawei.com> - 1.1.3-6
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:runc log forward to syslog

* Fri Nov 4 2022 zhongjiawei<zhongjiawei1@huawei.com> - 1.1.3-5
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:move install path to /usr/bin

* Tue Oct 18 2022 zhongjiawei<zhongjiawei1@huawei.com> - 1.1.3-4
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:move install path to /usr/bin

* Tue Aug 16 2022 zhongjiawei<zhongjiawei1@huawei.com> - 1.1.3-3
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix systemd cgroup after memory type changed

* Tue Aug 9 2022 zhongjiawei<zhongjiawei1@huawei.com> - 1.1.3-2
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:change Umask to 0022

* Tue Aug 9 2022 wangjunqi <wangjunqi@kylinos.cn> - 1.1.3-1
- update to 1.1.3

* Tue Aug 9 2022 zhongjiawei<zhongjiawei1@huawei.com> - 1.0.0.rc3-303
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:bump version to 303

* Fri Jul  8 2022 cenhuilin <cenhuilin@kylinos.cn> - 1.0.0.rc3-118
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix connect container failed when reading partially written state.json content 

* Mon Apr 11 2022 fushanqing <fushanqing@kylinos.cn> - 1.0.0.rc3-117
- add macro

* Thu Feb 10 2022 fushanqing <fushanqing@kylinos.cn> - 1.0.0.rc3-116
- remove "%global _bindir /usr/local/bin"

* Wed Jan 26 2022 songyanting <songyanting@huawei.com> - 1.0.0.rc3-115
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
