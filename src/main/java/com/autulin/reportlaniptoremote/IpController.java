package com.autulin.reportlaniptoremote;

import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.Date;

@RestController
@RequestMapping("ip")
public class IpController {

    private IpRecord ipRecord = new IpRecord();

    @PostMapping("")
    public String receiveIp(@RequestBody @Valid IpRecord ipRecord) {
        ipRecord.setDate(new Date());
        this.ipRecord = ipRecord;
        return "success";
    }

    @GetMapping("")
    public IpRecord getIpRecord() {
        return ipRecord;
    }
}
