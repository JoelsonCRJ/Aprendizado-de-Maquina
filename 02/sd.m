function [v4] = sd(a)
media = mean(a);
v1 = (a-media).^2;
v2 = sum(v1,1);
v3 = v2/length(a);
v4 = sqrt(v3);

if isnan(v4)
    v4 = 0;
end