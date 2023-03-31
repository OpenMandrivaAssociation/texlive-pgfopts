Name:		texlive-pgfopts
Version:	56615
Release:	2
Summary:	LaTeX package options with pgfkeys
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pgfopts
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfopts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfopts.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfopts.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The pgfkeys package (part of the pgf distribution) is a well-
designed way of defining and using large numbers of keys for
key-value syntaxes. However, pgfkeys itself does not offer
means of handling LaTeX class and package options. This package
adds such option handling to pgfkeys, in the same way that
kvoptions adds the same facility to the LaTeX standard keyval
package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pgfopts
%doc %{_texmfdistdir}/doc/latex/pgfopts
#- source
%doc %{_texmfdistdir}/source/latex/pgfopts

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
