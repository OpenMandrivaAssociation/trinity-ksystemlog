%bcond clang 1

# TDE variables
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif

%define tde_pkg ksystemlog
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Version:	0.3.2
Release:	%{?tde_version:%{tde_version}_}3
Summary:	System log viewer tool for Trinity
Group:		Applications/System
URL:		http://ksystemlog.forum-software.org

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/system/%{tarball_name}-%{tde_version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
ksystemlog is a system log viewer tool for Trinity.

This program is developed for being used by beginner users, which don't know
how to find information about their Linux system, and how the log files are in
their computer. But it is also designed for advanced users, who want to
quickly see problems occuring on their server.


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
# Missing category will make this fail.
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_prefix}/share/applications/tde/%{tde_pkg}.desktop"

%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README.md
%{tde_prefix}/bin/ksystemlog
%{tde_prefix}/share/applications/tde/ksystemlog.desktop
%{tde_prefix}/share/apps/ksystemlog/
%{tde_prefix}/share/config.kcfg/ksystemlog.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/ksystemlog.png
%{tde_prefix}/share/icons/hicolor/*/apps/ksystemlog.svgz
%{tde_prefix}/share/doc/tde/HTML/en/ksystemlog/
%{tde_prefix}/share/man/man1/ksystemlog.1*

