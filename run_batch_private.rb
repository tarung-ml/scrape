# Production run: Collecting profiles at current dir(outdir) for  set of saved html-files with paths provided in text file(urls)
 require 'yajl'
 outdir = "Documents"
 
 counter = 1
 inputfile = 'urls'
 lines = File.foreach(File.join(outdir,inputfile))
 currfile  = File.open(File.join(outdir,inputfile))
 URL_count = currfile.readlines.size

 while counter <= URL_count
 url = lines.next.delete!("\n")
 profile = Linkedin::Profile.get_profile("file:" + url)
 if(profile != nil)
 filename = "profile_" + counter.to_s + ".json"
 File.new(File.join(outdir,filename), "w")
 File.open(File.join(outdir,filename),"w") do |f|
 f.write(Yajl.dump(profile))
 end
 puts counter;
 counter = counter + 1;
 end
 end
