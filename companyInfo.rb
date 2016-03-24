# Given a set of company Linkedin URLs, collect the official website and company size.

require "mechanize"
require 'yajl'
outdir = "Ruby200/bin"

USER_AGENTS = ['Windows IE 6', 'Windows IE 7', 'Windows Mozilla', 'Mac Safari', 'Mac FireFox', 'Mac Mozilla', 'Linux Mozilla', 'Linux Firefox', 'Linux Konqueror']

def http_client
    Mechanize.new do |agent|
        agent.user_agent_alias = USER_AGENTS.sample
        agent.max_history = 0
        agent.keep_alive = false
    end
end

# get number of lines
inputfile = 'companies_demo.txt'
currfile  = File.open(File.join(outdir,inputfile))
URL_count = currfile.readlines.size
websites = Array.new(URL_count)
sizes = Array.new(URL_count)
founded = Array.new(URL_count)
lines = File.foreach(File.join(outdir,inputfile))
counter = 1
while counter <= URL_count
    url = lines.next.delete!("\n")
    comp = url.scan(/\d+/).first
    unless comp.nil? || nil == 0
        url = "http://www.linkedin.com//company/" + comp + "?trk=prof-exp-company-name"
        page = http_client.get(url)
        
        gettw = page.at(".website")
        unless gettw.nil? || nil == 0
            websites[counter] = gettw.text.split(' ',2)[1].strip
        end
        
        gettc = page.at(".company-size")
        unless gettc.nil? || nil == 0
            sizes[counter] = gettc.text.split(' ',2)[0].strip
        end
        
    end
    counter = counter+1
    puts counter-1;
end


filename = "sizes_demo"
File.new(File.join(outdir,filename), "w")
File.open(File.join(outdir,filename),"w") do |f|
    sizes.each { |element| f.puts(element) }
end


filename = "websites_demo"
File.new(File.join(outdir,filename), "w")
File.open(File.join(outdir,filename),"w") do |f|
    websites.each { |element| f.puts(element) }
end