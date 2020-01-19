function Data = OpenDataCommunites(fileName,threshold)

if (nargin == 2)                    % Two arguments are necessary 
    fid = fopen(fileName,'r');      % Open the file                                    % larger than is needed)
    nextLine = fgetl(fid);          % Read the first line from the file
    row = 1;
    Data = [];
while ~isequal(nextLine,-1)         % Loop while not at the end of the file
    if ~isempty(nextLine)           % Delete the empty lines     
                   
        coma = find(nextLine == ',');  % Find the separator comma
            
        
        %Data(row).communityname = nextLine(coma(3)+1:coma(4)-1);
        
        datatemp = [nextLine(1:coma(3)-1) nextLine(coma(4):end)];      
        
        coma = find( datatemp == ',');  % Find the separator comma
        
        Lost = find(datatemp == '?');  % Find the separator comma
        
        %datatemp(Lost) = -1;
        for index = 1:length(coma)
            
            if index>1
                if (isempty(str2num(datatemp(coma(index)-1))))
                    Data(row,index) = threshold;
                else   
                    Data(row,index) = str2num(datatemp(coma(index-1)+1:coma(index)-1));
                end
            else
                Data(row,index) = str2num(datatemp(1:coma(index)-1));
            end
            
            if index == length(coma)
                if (isempty(str2num(datatemp(coma(index)+1:end))))
                    Data(row,index+1) = threshold;
                else
                    Data(row,index+1) = str2num(datatemp(coma(index)+1:end));    
                end           
            end                
        end
        
            row = row+1;
            
            nextLine = fgetl(fid);          % Read the next line from the file
    else
        fclose(fid);                      % Close the file  
    end
end

end  
