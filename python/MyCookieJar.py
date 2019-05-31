import io

class MyCookieJar(MozillaCookieJar):
    def _really_load(self, f, filename, ignore_discard, ignore_expires):
        ignore_discard = True
        myfile = io.StringIO()
        for line in f:
            myfile.write(line.replace('\t0\t', '\t\t'))
        myfile.seek(0)
        f.close()
        super()._really_load(myfile, filename, ignore_discard, ignore_expires)

cj = MyCookieJar('cookies')
cj.load()