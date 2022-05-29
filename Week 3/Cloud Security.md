# Week 3: Cloud Security

Cloud computing is the delivery of hosted services, including software, hardware, and storage, over the Internet. The benefits of rapid deployment, flexibility, low up-front costs, and scalability, have made cloud computing virtually universal among organizations of all sizes, often as part of a hybrid/multi-cloud infrastructure architecture.

Cloud security refers to the technologies, policies, controls, and services that protect cloud data, applications, and infrastructure from threats.

## Real Cloud Based Attacks

- Please watch this brief video on cloud security and cloud based attacks from Microsoft - Really interesting!

- Real examples of hacking and malware attacks then what Microsoft did to stop them - https://www.youtube.com/watch?v=y8Z_0CEJEQY 

- Please take a minute to look at the Cloud Security Alliance website.  They provide a great set of resources to help understand and manage cloud security.

  https://cloudsecurityalliance.org/
  
 ### Lecture Slides

These lecture slides are also available at: https://academics.uccs.edu/greg/Coursera/Practical_Computer_Security/Course2/

## `What is Infrastructure as a Service?` 

The term Infrastructure as a Service, or IaaS (also, occasionally called Hardware as a Service), falls within the subject area of Cloud Computing and is sometimes accompanied by the terms Platform as a Service (PaaS) and Software as a Service (SaaS).  

Infrastructure as a Service describes a model where organizations outsource hardware requirements such as database storage, networking components, servers, and database/server virtualization to an outside vendor . The organization will often pay on a per-use basis meaning the vendor charges based on actual storage space used in conjunction with data transmission rates.   The vendor provides the equipment and is responsible for its maintenance which typically offers dynamic scalability as the purchasing organization’s hardware requirements increase.  

Infrastructure as a Service means the companies can focus on creating applications without incurring the upfront costs of purchasing and maintaining underutilized hardware.

**Infrastructure as a service (IaaS)** is a form of cloud computing that provides virtualized computing resources over the internet. IaaS is one of the three main categories of cloud computing services, alongside software as a service (SaaS) and platform as a service (PaaS).

In the _IaaS model_, the cloud provider manages IT infrastructures such as storage, server and networking resources, and delivers them to subscriber organizations via virtual machines accessible through the internet. IaaS can have many benefits for organizations, such as potentially making workloads faster, easier, more flexible and more cost efficient.
IaaS architecture

In an _IaaS_ service model, a cloud provider hosts the infrastructure components that are traditionally present in an on-premises data center. This includes servers, storage and networking hardware, as well as the **virtualization** or **hypervisor** layer.

The following diagram shows a simplified view of the 3 main layers of cloud computing and how each layer builds upon the one which precedes it.  

![layers of cloud computing](https://www.modernanalyst.com/Portals/0/images/iaas-paas-saas.jpg)


## Cloud Security is a Shared Responsibility

Cloud security is a responsibility that is shared between the cloud provider and the customer. There are basically three categories of responsibilities in the Shared Responsibility Model: responsibilities that are always the provider’s, responsibilities that are always the customer’s, and responsibilities that vary depending on the service model: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), or Software as a Service (SaaS), such as cloud email.

The security responsibilities that are always the provider’s are related to the safeguarding of the infrastructure itself, as well as access to, patching, and configuration of the physical hosts and the physical network on which the compute instances run and the storage and other resources reside.

The security responsibilities that are always the customer’s include managing users and their access privileges (identity and access management), the safeguarding of cloud accounts from unauthorized access, the encryption and protection of cloud-based data assets, and managing its security posture (compliance).
The Top 7 Advanced Cloud Security Challenges

Because the public cloud does not have clear perimeters, it presents a fundamentally different security reality. This becomes even more challenging when adopting modern cloud approaches such as automated Continuous Integration and Continuous Deployment (CI/CD) methods, distributed serverless architectures, and ephemeral assets like Functions as a Service and containers.

### Some of the advanced cloud-native security challenges and the multiple layers of risk faced by today’s cloud-oriented organizations include:

    Increased Attack Surface

    The public cloud environment has become a large and highly attractive attack surface for hackers who exploit poorly secured cloud ingress ports in order to access and disrupt workloads and data in the cloud. Malware, Zero-Day, Account Takeover and many other malicious threats have become a day-to-day reality.
    Lack of Visibility and Tracking

    In the IaaS model, the cloud providers have full control over the infrastructure layer and do not expose it to their customers. The lack of visibility and control is further extended in the PaaS and SaaS cloud models. Cloud customers often cannot effectively identify and quantify their cloud assets or visualize their cloud environmets.
    Ever-Changing Workloads

    Cloud assets are provisioned and decommissioned dynamically—at scale and at velocity. Traditional security tools are simply incapable of enforcing protection policies in such a flexible and dynamic environment with its ever-changing and ephemeral workloads.
    DevOps, DevSecOps and Automation

    Organizations that have embraced the highly automated DevOps CI/CD culture must ensure that appropriate security controls are identified and embedded in code and templates early in the development cycle. Security-related changes implemented after a workload has been deployed in production can undermine the organization’s security posture as well as lengthen time to market.
    Granular Privilege and Key Management

    Often cloud user roles are configured very loosely, granting extensive privileges beyond what is intended or required. One common example is giving database delete or write permissions to untrained users or users who have no business need to delete or add database assets. At the application level, improperly configured keys and privileges expose sessions to security risks.
    Complex Environments

    Managing security in a consistent way in the hybrid and multicloud environments favored by enterprises these days requires methods and tools that work seamlessly across public cloud providers, private cloud providers, and on-premise deployments—including branch office edge protection for geographically distributed organizations.
    Cloud Compliance and Governance

    All the leading cloud providers have aligned themselves with most of the well-known accreditation programs such as PCI 3.2, NIST 800-53, HIPAA and GDPR. 
    However, customers are responsible for ensuring that their workload and data processes are compliant.
    Given the poor visibility as well as the dynamics of the cloud environment, the compliance audit process becomes close to mission impossible unless tools are used to achieve continuous compliance checks and issue real-time alerts about misconfigurations.

## Zero Trust and Why You Should Embrace It

The term Zero Trust was first introduced in 2010 by John Kindervag who, at that time, was a senior Forrester Research analyst. The basic principle of Zero Trust in cloud security is not to automatically trust anyone or anything within or outside of the network—and verify (i.e., authorize, inspect and secure) everything.

Zero Trust, for example, promotes a least privilege governance strategy whereby users are only given access to the resources they need to perform their duties. Similarly, it calls upon developers to ensure that web-facing applications are properly secured.  For example, if the developer has not blocked ports consistently or has not implemented permissions on an “as needed” basis, a hacker who takes over the application will have privileges to retrieve and modify data from the database.

In addition, Zero Trust networks utilize micro-segmentation to make cloud network security far more granular. Micro-segmentation creates secure zones in data centers and cloud deployments thereby segmenting workloads from each other, securing everything inside the zone, and applying policies to secure traffic between zones.
The 6 Pillars of Robust Cloud Security

While cloud providers such as Amazon Web Services (AWS), Microsoft Azure (Azure), and Google Cloud Platform (GCP) offer many cloud native security features and services, supplementary third-party solutions are essential to achieve enterprise-grade cloud workload protection from breaches, data leaks, and targeted attacks in the cloud environment. Only an integrated cloud-native/third-party security stack provides the centralized visibility and policy-based granular control necessary to deliver the following industry best practices:

    Granular, policy-based IAM and authentication controls across complex infrastructures

    Work with groups and roles rather than at the individual IAM level to make it easier to update IAM definitions as business requirements change.
    Grant only the minimal access privileges to assets and APIs that are essential for a group or role to carry out its tasks. The more extensive privileges,
    the higher the levels of authentication. And don’t neglect good IAM hygiene, enforcing strong password policies, permission time-outs, and so on.
    Zero-trust cloud network security controls across logically isolated networks and micro-segments

    Deploy business-critical resources and apps in logically isolated sections of the provider’s cloud network, such as Virtual Private Clouds (AWS and Google) 
    or vNET (Azure).
    Use subnets to micro-segment workloads from each other, with granular security policies at subnet gateways. Use dedicated WAN links in hybrid architectures,
    and use static user-defined routing configurations to customize access to virtual devices, 
    virtual networks and their gateways, and public IP addresses.
    Enforcement of virtual server protection policies and processes such as change management and software updates:

    Cloud security vendors provide robust Cloud Security Posture Management, consistently applying governance and compliance rules and templates 
    when provisioning virtual servers, auditing for configuration deviations, and remediating automatically where possible.
    Safeguarding all applications (and especially cloud-native distributed apps) with a next-generation web application firewall

    This will granularly inspect and control traffic to and from web application servers, automatically updates WAF rules in response to traffic behavior changes,
    and is deployed closer to microservices that are running workloads.
    Enhanced data protection

    Enhanced data protection with encryption at all transport layers, secure file shares and communications, continuous compliance risk management, 
    and maintaining good data storage resource hygiene such as detecting misconfigured buckets and terminating orphan resources.
    Threat intelligence that detects and remediates known and unknown threats in real-time

    Third-party cloud security vendors add context to the large and diverse streams of cloud-native logs by intelligently 
    cross-referencing aggregated log data with internal data such as asset and configuration management systems, vulnerability scanners, etc. 
    and external data such as public threat intelligence feeds, geolocation databases, etc. They also provide tools that help visualize
    and query the threat landscape and promote quicker incident response times. 
    AI-based anomaly detection algorithms are applied to catch unknown threats, which then undergo forensics analysis to determine their risk profile. 
    Real-time alerts on intrusions and policy violations shorten times to remediation, sometimes even triggering auto-remediation workflows.

 across all the pillars of cloud security: access control, network security, virtual server compliance, workload and data protection, and threat intelligence.

![cloud security pillars diagram](https://www.checkpoint.com/wp-content/uploads/cloud-security-pillars-diagram.jpg)

